# 🏦 Real-Time Transaction Compliance Auditor (RAG System)

An AI decision-support system that evaluates financial transaction scenarios against a compliance manual using Retrieval-Augmented Generation (RAG).

Instead of searching policies manually, users describe a situation in natural language and receive a compliance assessment grounded in official rules.

---

## ✨ Key Features

- 📄 Policy-aware responses from a compliance manual (PDF)
- 🔍 Semantic search over Q&A-style regulations
- ⚖️ Compliance reasoning for real transaction scenarios
- 🧠 Local LLM support via Ollama (no API cost required)
- 📊 Returns similarity score and answer source (policy vs general)
- 🌐 Full-stack web application (React + FastAPI)

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

```
Client wants to transfer $50,000 to Cayman Islands.
Customer has 2 years of account history.
```

### Output

Structured response:

```json
{
  "source": "policy",
  "similarity": 0.63,
  "answer": "FLAGGED. Transfers to high-risk jurisdictions require enhanced due diligence."
}
```

If no policy is relevant:

```json
{
  "source": "general",
  "answer": "General guidance..."
}
```

---

## 🏗️ High-Level Architecture

```
User (Browser)
      ↓
React Frontend
      ↓ HTTP
FastAPI Backend
      ↓
RAG Pipeline
      ↓
Vector Database (Pinecone)
      ↓
Local LLM (Ollama)
      ↓
Response
```

---

## 🔄 RAG Pipeline Flow

### 1) Ingestion (One-Time)

```
PDF Compliance Manual
        ↓
Text Extraction
        ↓
Q&A Chunking
        ↓
Embeddings (HuggingFace)
        ↓
Pinecone Vector Index
```

### 2) Query Time

```
User Scenario
      ↓
Embedding
      ↓
Vector Search
      ↓
Relevant Policies Retrieved
      ↓
LLM Reasoning (Ollama)
      ↓
Compliance Assessment
```

---

## 🧠 Tech Stack

### Frontend
- React
- Fetch API

### Backend
- FastAPI
- LangChain (RAG orchestration)

### AI Components
- **LLM:** Ollama (Llama 3 / Mistral)
- **Embeddings:** Sentence Transformers (MiniLM)
- **Vector DB:** Pinecone

### Data Processing
- PyPDFLoader (LangChain)

---

## 📂 Project Structure

```
compliance-auditor/
│
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entry point
│   │   ├── ingest.py        # PDF → vector DB
│   │   ├── rag_pipeline.py  # Retrieval + reasoning
│   │   ├── config.py        # Settings
│   │   └── models.py        # API schemas
│   └── data/                # Compliance manual
│
├── frontend/
│   └── src/
│       ├── App.js           # UI
│       └── api.js           # Backend calls
│
└── docker-compose.yml
```

---

## 🚀 How to Run Locally

### 1️⃣ Start Ollama

```
ollama pull llama3
```

---

### 2️⃣ Start Backend

```
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### 3️⃣ Ingest Compliance Manual (one-time)

Open:

```
http://localhost:8000/docs
```

Run:

```
POST /ingest
```

---

### 4️⃣ Start Frontend

```
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🧪 Example Scenario to Test

```
Client wants to transfer $50,000 to Cayman Islands.
```

---

## 🏆 Why This Project Matters

This architecture mirrors real systems used in:

- Financial compliance automation  
- RegTech platforms  
- Legal document intelligence  
- Enterprise knowledge assistants  

---

## 📌 Future Improvements

- Risk scoring (Approved / Flagged)
- Policy citations with page numbers
- Multi-document support
- Conversation memory
- Cloud deployment

---

## 📄 License

MIT (or your preferred license)

---

## 👤 Author

Your Name  
GitHub: https://github.com/yourusername
