# AI-Powered NL → SQL Analytics Platform

An intelligent data analytics system that allows users to query a MySQL database using natural language.
The system converts user queries into SQL using a local LLM (Qwen via Ollama) and returns structured results.

---

## 🧠 Problem

Non-technical users struggle to write SQL queries.

👉 This system solves it by enabling:

**Natural Language → SQL → Insights**

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** MySQL
* **LLM:** Qwen2.5:3B (Ollama)

---

## 🏗️ Architecture

```
User → Streamlit → LLM (Qwen) → SQL → MySQL → Result
```

---

## 📂 Project Structure

```
project/
│
├── app.py          # Streamlit UI
├── db.py           # Database logic
├── llm.py          # LLM integration
├── prompt.py       # Prompt engineering
├── utils.py        # Helper functions
├── requirements.txt
└── README.md
```

---

## ▶️ Setup Instructions

### 1. Clone repo

```
git clone <repo_url>
cd project
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Start Ollama

```
ollama serve
```

### 4. Run model

```
ollama run qwen2.5:3b
```

### 5. Run app

```
streamlit run app.py
```

---

## 🔥 Features

* Natural Language → SQL conversion
* Multi-table JOIN support
* Aggregation (SUM, COUNT, etc.)
* Prompt-engineered accuracy
* MySQL integration

---

## Example Queries

| Natural Language | Generated SQL |
|----------------|--------------|
| Show all customers | SELECT * FROM customers; |
| Total sales | SELECT SUM(total_amount) FROM orders; |
| Top 5 customers | GROUP BY + ORDER BY + LIMIT |
| Sales by department | Multi-table JOIN |

---

## Safety & Validation

- Blocks:
  - DROP
  - DELETE
  - UPDATE
  - TRUNCATE

- Ensures:
  - Read-only queries
  - Controlled execution

---

## ⚠️ Limitations

* LLM may generate incorrect queries in edge cases
* Depends on prompt quality
* No dynamic schema support yet
* Limited scalability (local setup)

---

## 🚀 Future Improvements

* Dynamic schema detection
* RAG-based table retrieval
* Query validation & auto-correction
* Dashboard & charts
* Cloud deployment

---

## 🎯 Key Learnings

* Prompt engineering for structured tasks
* LLM integration with backend systems
* SQL query generation & optimization
* Building end-to-end AI systems

---

## 💡 Conclusion

This project demonstrates how AI can bridge the gap between users and data systems by enabling natural language querying over structured databases.

---

## 👨‍💻 Author

**Mazhar Kakar**
