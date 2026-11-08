// tools/test-chat.js — local smoke test for api/chat.js (no server needed).
// Usage: node tools/test-chat.js "your question" ["optional selected text"]
const handler = require("../api/chat.js");

function makeRes() {
  let body = "";
  return {
    statusCode: 200,
    headers: {},
    setHeader(k, v) { this.headers[k.toLowerCase()] = v; },
    status(c) { this.statusCode = c; return this; },
    json(o) { body = JSON.stringify(o); this.end(); return this; },
    write(chunk) { body += chunk; },
    end() { this._body = body; },
  };
}

(async () => {
  const q = process.argv[2] || "What is the difference between == and === in PHP?";
  const sel = process.argv[3] || "";
  const req = {
    method: "POST",
    headers: { "content-type": "application/json", host: "localhost:3000", origin: "http://localhost:3000" },
    body: { q, sel, page: "Module 3 — PHP", section: "Comparison operators: == converts types, === compares value and type.", outline: "- 2.4 Operators\n- 3.1 Answer bank" },
  };
  const res = makeRes();
  const t0 = Date.now();
  await handler(req, res);
  const ms = Date.now() - t0;

  if (res.statusCode !== 200) {
    console.error("HTTP", res.statusCode, res._body);
    process.exit(1);
  }
  const text = (res._body || "")
    .split("\n")
    .filter((l) => l.startsWith("data:"))
    .map((l) => l.slice(5).trim())
    .filter((d) => d && d !== "[DONE]")
    .map((d) => { try { return JSON.parse(d).d || ""; } catch { return ""; } })
    .join("");

  console.log(`status=${res.statusCode} time=${ms}ms chars=${text.length}`);
  console.log("--- answer ---");
  console.log(text || "(empty)");
})();
