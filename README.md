# 🚀 Financial Document Management API with Semantic Search (RAG)

## 📌 Overview

This project is a **FastAPI-based Financial Document Management System** enhanced with **AI-powered semantic search using Retrieval-Augmented Generation (RAG)**.

It allows organizations to:

* Upload and manage financial documents (reports, invoices, contracts)
* Perform **semantic search** (not just keyword search)
* Enforce **Role-Based Access Control (RBAC)**
* Retrieve meaningful insights using embeddings and vector search

---

## 🧠 Key Features

### 🔐 Authentication & Authorization

* JWT-based authentication
* Role-Based Access Control (RBAC)
* Roles:

  * **Admin** → Full access
  * **Analyst** → Upload/edit documents
  * **Auditor** → Review documents
  * **Client** → View documents

---

### 📄 Document Management

* Upload financial documents
* Store metadata:

  * document_id
  * title
  * company_name
  * document_type
  * uploaded_by
  * created_at
* Retrieve all documents
* Get document by ID
* Delete documents
* Search documents by metadata

---

### 🧠 Semantic Search (RAG)

* Converts documents into embeddings
* Stores embeddings in vector database
* Retrieves relevant content using similarity search

#### 🔄 RAG Pipeline:

```
Document → Text Extraction → Chunking → Embedding → Vector DB
```

#### 🔍 Search Pipeline:

```
Query → Embedding → Vector Search → Top Results → Response
```

---

## 🏗️ Tech Stack

| Layer          | Technology           |
| -------------- | -------------------- |
| Backend        | FastAPI              |
| Database       | PostgreSQL           |
| Vector DB      | Qdrant               |
| AI Model       | SentenceTransformers |
| Authentication | JWT                  |
| ORM            | SQLAlchemy           |

---

## 📁 Project Structure

```
financial-rag-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/vaijeenathgolhar/financial-rag-api.git
cd financial-rag-api
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/finance_db
SECRET_KEY=your_secret_key
QDRANT_HOST=localhost
QDRANT_PORT=6333
COLLECTION_NAME=financial_docs
```

---

### 5️⃣ Run PostgreSQL

Make sure PostgreSQL is running and database is created:

```
CREATE DATABASE finance_db;
```

---

### 6️⃣ Run Qdrant (Vector DB)

Using Docker:

```
docker run -p 6333:6333 qdrant/qdrant
```

---

### 7️⃣ Run Backend Server

```
uvicorn app.main:app --reload
```

---

### 8️⃣ Access API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🔌 API Endpoints

### 🔐 Authentication

* `POST /auth/register`
* `POST /auth/login`

---

### 📄 Documents

* `POST /documents/upload`
* `GET /documents`
* `GET /documents/{id}`
* `DELETE /documents/{id}`
* `GET /documents/search`

---

### 🧠 RAG (Semantic Search)

* `POST /rag/search`

Example:

```json
{
  "query": "financial risk due to high debt"
}
```

---

## 🧪 Example Workflow

1. Register a user
2. Login to get JWT token
3. Upload document
4. Perform semantic search

---

## 🧠 How Semantic Search Works

* Text is converted into vectors using SentenceTransformers
* Stored in Qdrant vector database
* Query is also converted into vector
* Similarity search retrieves relevant chunks

---

## 🔐 Security Best Practices

* Secrets stored in `.env` file
* `.env` excluded using `.gitignore`
* No credentials hardcoded

---

## 🚀 Future Enhancements

* 📄 PDF parsing support (PyMuPDF)
* 💬 Chat with documents (LLM integration)
* 📊 Dashboard UI (React)
* ☁️ Deployment (AWS / Render / Docker)
* 🔎 Advanced filtering & pagination

---

## 🧾 Resume Description (Use This)

> Built a FastAPI-based financial document management system with semantic search using RAG. Implemented JWT authentication, RBAC, and vector search using Qdrant with SentenceTransformers to enable intelligent document retrieval.

---

## 👨‍💻 Author

**Vaijeenath Golhar**

* LinkedIn: https://linkedin.com/in/your-profile
* GitHub: https://github.com/vaijeenathgolhar

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
