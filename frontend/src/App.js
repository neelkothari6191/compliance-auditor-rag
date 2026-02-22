import React, { useState } from "react";
import { query } from "./api";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  async function ask() {
    const r = await query(text);
    setResult(r);
  }

  return (
    <div style={{padding: 20}}>
      <h1>Compliance Auditor</h1>

      <textarea
        rows={5}
        value={text}
        onChange={e => setText(e.target.value)}
        style={{width: "100%"}}
      />

      <button onClick={ask}>Submit</button>

      {result && (
        <div>
          <h3>Source: {result.source}</h3>
          <pre>{result.answer}</pre>
        </div>
      )}
    </div>
  );
}
