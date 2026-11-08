// api/chat.js — study assistant for the notes site.
// Streams answers from the opencode-go endpoint (OpenAI-compatible).
// Env: OPENCODE_GO_API_KEY (required), OPENCODE_GO_BASE_URL, CHAT_MODEL,
//      CHAT_ALLOW_ORIGINS (optional comma list).

const BASE = process.env.OPENCODE_GO_BASE_URL || "https://opencode.ai/zen/go/v1";
const MODEL = process.env.CHAT_MODEL || "deepseek-v4.1-flash";
const KEY = process.env.OPENCODE_GO_API_KEY || process.env.OPENCODE_API_KEY || "";

const LIMITS = { q: 600, sel: 3000, section: 3000, outline: 1200 };

// opencode-go routes on a session header; one id per browser session is enough.
const crypto = require("crypto");
const FALLBACK_SESSION = crypto.randomUUID();

// Best-effort abuse guard: per-instance, resets on cold start. Not a security
// boundary — it only stops a leaked URL from being hammered casually.
const hits = new Map();
function rateLimited(ip) {
  const now = Date.now();
  const win = hits.get(ip) || [];
  const recent = win.filter((t) => now - t < 60_000);
  recent.push(now);
  hits.set(ip, recent);
  if (hits.size > 500) for (const [k, v] of hits) if (!v.some((t) => now - t < 60_000)) hits.delete(k);
  return recent.length > 20;
}

function allowedOrigin(req) {
  const origin = req.headers.origin || "";
  const allow = (process.env.CHAT_ALLOW_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
  if (!origin) return true; // curl / same-origin GET without Origin
  const host = req.headers.host || "";
  try {
    const o = new URL(origin).host;
    if (allow.length) return allow.includes(origin) || allow.includes(o);
    if (o === host) return true;
    return o.endsWith(".vercel.app") || o === "localhost" || o.startsWith("localhost:") ||
           o === "127.0.0.1" || o.startsWith("127.0.0.1:");
  } catch {
    return false;
  }
}

const trim = (v, n) => (typeof v === "string" ? v.trim().slice(0, n) : "");

function systemPrompt(page) {
  return [
    "You are the study assistant embedded in Haze's 20CST461 Web Technologies notes (KTU ESE: 3 h, Part A 3-mark short answers, Part B 14-mark long answers).",
    "Answer the doubt directly. No preamble, no restating the question.",
    "Default: at most 90 words — this is a quick doubt, not an essay. Bullets when listing, exact syntax and one short example for code doubts.",
    "Prefer the supplied page context. If the answer is not in it, open with 'Not on this page:' and then answer from standard web-development knowledge in one or two lines.",
    "If the student is preparing an exam answer, say how it would be written for marks (e.g. '3 points, ~3 lines').",
    page ? `Current page: ${page}` : "",
  ].filter(Boolean).join("\n");
}

function userPrompt(body) {
  const parts = [];
  if (body.outline) parts.push(`Page outline:\n${body.outline}`);
  if (body.section) parts.push(`Section the student is reading:\n${body.section}`);
  if (body.sel) parts.push(`Selected text:\n"""\n${body.sel}\n"""`);
  parts.push(`Question: ${body.q}`);
  return parts.join("\n\n");
}

module.exports = async function handler(req, res) {
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Origin", req.headers.origin || "*");
    res.setHeader("Access-Control-Allow-Headers", "content-type");
    res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
    return res.status(204).end();
  }
  if (req.method !== "POST") return res.status(405).json({ error: "POST only" });

  if (!KEY) return res.status(500).json({ error: "OPENCODE_GO_API_KEY is not set on this deployment" });
  if (!allowedOrigin(req)) return res.status(403).json({ error: "origin not allowed" });

  const ip = (req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "unknown";
  if (rateLimited(ip)) return res.status(429).json({ error: "too many questions, wait a minute" });

  let body;
  try {
    body = typeof req.body === "string" ? JSON.parse(req.body) : req.body || {};
  } catch {
    return res.status(400).json({ error: "bad json" });
  }

  const q = trim(body.q, LIMITS.q);
  if (!q) return res.status(400).json({ error: "empty question" });

  const payload = {
    model: MODEL,
    stream: true,
    temperature: 0.2,
    max_tokens: 500,
    messages: [
      { role: "system", content: systemPrompt(trim(body.page, 200)) },
      {
        role: "user",
        content: userPrompt({
          q,
          sel: trim(body.sel, LIMITS.sel),
          section: trim(body.section, LIMITS.section),
          outline: trim(body.outline, LIMITS.outline),
        }),
      },
    ],
  };

  const session = (typeof (body.sid || body.session) === "string" && /^[A-Za-z0-9-]{8,64}$/.test(body.session))
    ? (body.sid || body.session)
    : FALLBACK_SESSION;

  let upstream;
  try {
    upstream = await fetch(`${BASE}/chat/completions`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        authorization: `Bearer ${KEY}`,
        "x-opencode-session": session,
      },
      body: JSON.stringify(payload),
    });
  } catch (err) {
    return res.status(502).json({ error: `upstream unreachable: ${err.message}` });
  }

  if (!upstream.ok || !upstream.body) {
    const text = await upstream.text().catch(() => "");
    return res.status(502).json({ error: `upstream ${upstream.status}`, detail: text.slice(0, 400) });
  }

  res.setHeader("Content-Type", "text/event-stream; charset=utf-8");
  res.setHeader("Cache-Control", "no-cache, no-transform");
  res.setHeader("Connection", "keep-alive");
  res.setHeader("X-Accel-Buffering", "no");

  const reader = upstream.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n");
      buffer = lines.pop() || "";
      for (const line of lines) {
        const l = line.trim();
        if (!l.startsWith("data:")) continue;
        const data = l.slice(5).trim();
        if (data === "[DONE]") continue;
        try {
          const json = JSON.parse(data);
          const delta = json.choices?.[0]?.delta?.content;
          if (delta) res.write(`data: ${JSON.stringify({ d: delta })}\n\n`);
        } catch {
          /* ignore keep-alive fragments */
        }
      }
    }
  } catch (err) {
    res.write(`data: ${JSON.stringify({ error: err.message })}\n\n`);
  }
  res.write("data: [DONE]\n\n");
  res.end();
};
