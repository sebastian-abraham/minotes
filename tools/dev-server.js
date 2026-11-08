// tools/dev-server.js — local stand-in for Vercel: static files + /api/chat.
// Usage: OPENCODE_GO_API_KEY=... node tools/dev-server.js [port]
const http = require("http");
const fs = require("fs");
const path = require("path");
const handler = require("../api/chat.js");

const ROOT = path.join(__dirname, "..");
const PORT = Number(process.argv[2] || 8787);
const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".json": "application/json",
  ".css": "text/css",
  ".js": "text/javascript",
  ".svg": "image/svg+xml",
  ".md": "text/markdown; charset=utf-8",
};

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || "localhost"}`);

  if (url.pathname === "/api/chat") {
    // mimic Vercel: parsed body for application/json
    let raw = "";
    for await (const chunk of req) raw += chunk;
    const q = Object.assign(req, {
      body: raw ? safeJson(raw) : {},
      query: Object.fromEntries(url.searchParams),
    });
    return handler(q, res);
  }

  let p = path.join(ROOT, decodeURIComponent(url.pathname));
  if (p.endsWith("/")) p = path.join(p, "index.html");
  if (!fs.existsSync(p) || fs.statSync(p).isDirectory()) p = path.join(ROOT, "index.html");
  if (!p.startsWith(ROOT)) return res.writeHead(403).end("forbidden");

  res.writeHead(200, { "content-type": TYPES[path.extname(p)] || "application/octet-stream" });
  fs.createReadStream(p).pipe(res);
});

function safeJson(s) {
  try { return JSON.parse(s); } catch { return {}; }
}

server.listen(PORT, () => console.log(`dev server on http://localhost:${PORT}`));
