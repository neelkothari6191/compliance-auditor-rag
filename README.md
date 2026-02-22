# 🏦 Real-Time Transaction Compliance Auditor (RAG System)

An AI decision-support system that evaluates financial transaction scenarios against a compliance manual using Retrieval-Augmented Generation (RAG).

Instead of searching policies manually, users describe a situation in natural language and receive a compliance assessment grounded in official rules.

---

## ✨ Key Features

- 📄 Policy-aware responses from a compliance manual (PDF)
- 🔍 Semantic search over Q&A-style regulations
- ⚖️ Compliance reasoning for real transaction scenarios
- 🧠 Local LLM support (Ollama) — no API cost required
- 📊 Returns similarity score + answer source (policy vs general)
- 🌐 Full-stack web app (React + FastAPI)

---

## 🧩 Use Case

Designed for roles such as:

- Bank customer service agents  
- Junior brokers  
- Compliance officers  
- AML/KYC analysts  

Example query:

> “Client wants to transfer $50,000 to the Cayman Islands for a real estate purchase.”

The system retrieves relevant rules and evaluates compliance risk.

---

## 📥 Input & 📤 Output

### Input

Natural-language transaction scenario:
