const API = "http://localhost:8000";

export async function query(question) {
  const res = await fetch(`${API}/query`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ question })
  });
  return res.json();
}
