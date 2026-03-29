# AI-Powered Data Analytics Platform (NATURAL LANGUAGE → SQL)

An intelligent data analytics platform that allows non-technical users to query a relational database using natural language.

This system converts user questions into SQL queries using a QWEN2.5:3B LLM MODEL built and developed by the (Qwen Team at Alibaba Cloud) and executes them on a MySQL database, returning structured results in real time.

---

## Problem Statement

Traditional data analytics tools require SQL knowledge, making them inaccessible to non-technical users.

This project solves that by enabling:

=> Natural Language → SQL → Insights

---

## Tech Stack

| Layer        | Technology |
|--------------|-----------|
| Frontend     | Streamlit |
| Backend      | Python |
| Database     | MySQL |
| LLM Engine   | Ollama (Local) |
| Model        | Qwen2.5:3B |
| API Layer    | REST (localhost:11434) |

---

## Architecture

User Input (Natural Language)
↓
Streamlit UI
↓
Prompt Engineering Layer
↓
Ollama (Qwen LLM)
↓
Generated SQL Query
↓
Query Validation Layer
↓
MySQL Database
↓
Results → DataFrame → UI

---

## Database Schema

The system is built on a normalized relational schema:

- Customers
- Orders
- Order Items
- Products
- Categories
- Departments

Supports complex joins and hierarchical relationships.

---

## Key Features

### Natural Language to SQL
- Converts user queries into optimized SQL
- Supports aggregation, joins, filtering

---

### Multi-Table Query Support
- Handles complex joins across multiple tables
- Understands relational dependencies

---

### Local LLM (No API Cost)
- Runs fully offline using Ollama
- No external API dependency

---

### Query Validation Layer
- Blocks dangerous queries (DROP, DELETE, etc.)
- Ensures only safe SELECT operations

---

### Structured Output
- Displays results with proper column names
- Uses Pandas DataFrame for readability
- Download option as CSV file

---

### Prompt Engineering
- Schema-aware prompt design
- Few-shot learning for higher accuracy

---

### Suggested Queries (UX Feature)
- Predefined analytics queries
- Improves usability for non-technical users

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

## ⚡ Performance Optimizations

- Query validation before execution
- Avoids SELECT *
- Supports LIMIT enforcement
- Ready for indexing improvements

---

## Project Structure

project/
│
├── app.py # Streamlit UI
├── db.py # Database logic
├── llm.py # LLM integration (Ollama)
├── prompt.py # Prompt engineering
├── utils.py # Helper functions
├── requirements.txt
└── README.md


---

## ▶️ Setup Instructions

### 1. Clone repository

```bash
git clone <repo_url>
cd project

2. Install dependencies
pip install -r requirements.txt

3. Start Ollama
ollama serve

4. Run LLM
ollama run qwen2.5:3b

5. Start application
streamlit run app.py

---

### Design Decisions
✔ Why Local LLM?
Avoid API cost
Full control
Privacy-friendly

✔ Why Prompt Engineering instead of Fine-tuning?
Faster iteration
Lower compute requirement
Easier debugging

✔ Why MySQL?
Industry standard
ACID compliance
Supports complex joins

=> Limitations / Drawbacks
1. LLM Accuracy
May generate incorrect joins in edge cases
Depends heavily on prompt quality

2. Performance Constraints
Local model (3B) has limited reasoning power
Slower than cloud LLMs

3. No Semantic Layer
Business logic not abstracted
Requires schema understanding

4. Limited Error Recovery
Basic retry mechanism
No advanced SQL correction loop

5. Concurrency Limitations
Not optimized for multi-user scaling
No connection pooling yet

=> Future Improvements
1. Fine-tuned SQL Model
Train model on SQL dataset
Improve query accuracy

2. Dynamic Schema Injection
Auto-fetch schema from MySQL
Remove hardcoded schema

3. Query Correction Loop
Detect SQL errors
Re-generate corrected query

4. Visualization Layer
Charts (bar, pie, line)
Dashboard UI

5. Role-Based Access Control
Restrict sensitive queries
User authentication

6. Caching Layer
Cache frequent queries
Reduce latency

7. Query Explain Feature
Show execution plan
Improve performance debugging

8. Multi-User Support
Connection pooling
Async query handling

9. Hybrid Retrieval (RAG)
Combine schema + metadata
Improve context understanding

10. Cloud Deployment
Dockerize application
Deploy on AWS / GCP

=> Key Learning Outcomes
Prompt Engineering for structured tasks
LLM integration with backend systems
Database design & query optimization
Building end-to-end AI systems

=> Conclusion

This project demonstrates how AI can bridge the gap between non-technical users and structured data systems.
It combines:

👉 LLM + SQL + Backend Engineering + UI

to create a powerful, scalable data analytics solution.

=> Author
Mazhar Kakar





















- START OLLAMA: ollama serve
- RUN AND DOWNLOAD QWEN2.5:3B: ollama run qwen2.5:3b
- SHOW INSTALLED MODELS: ollama list
- SHOW AVILABLE MODELS: ollama search qwen
- MODEL SAVED IN THIS FILE PATH: ~/.ollama/models
- CHECK RUNNING MODELS: ollama ps
- STOP RUNNING MODEL: ollama stop qwen2.5:3b
- STOP EVERYTHING: pkill ollama
- STOP THE OLLAMA SERVICE: sudo systemctl stop ollama OR pkill ollama

- CREATE PYTHON VIRTUAL ENVIRONEMENT: python3 -m venv newenv
- ACTIVATE VIRTUAL ENVIRONEMENT: source .venv/bin/activate
- Linux (systemd): Run sudo systemctl stop ollama








🟢 LEVEL 1 — EASY (Basic SELECT)
Show all customers
Show all products with their price
List all orders with order date and status
Show all categories
Show all departments
🟡 LEVEL 2 — FILTERING
Show all customers from city "Mumbai"
Show all orders with status "completed"
Show products with price greater than 1000
Show customers whose pincode is 422001
Show orders placed after 2023-01-01
🟠 LEVEL 3 — AGGREGATION
Count total number of customers
Find total number of orders
Find total sales amount (sum of order_items total_amount)
Find average product price
Count number of products in each category
🔵 LEVEL 4 — GROUP BY + JOIN
Show total orders per customer (with customer name)
Show total sales amount per customer
Show total number of products in each department
Show total sales by each category
🔴 LEVEL 5 — ADVANCED JOIN + LOGIC
Show total sales by each department
🔥 BONUS (VERY IMPORTANT — REAL TEST)

👉 These are edge cases (LLM usually fails here)

🧠 Hard 1
Find customers who never placed any order
🧠 Hard 2
Find products that were never ordered
🧠 Hard 3
Show top 5 customers by total spending
🧠 Hard 4
Show top 3 most sold products by quantity
🧠 Hard 5
Show department with highest total sales
🧠 Hard 6 (Multi-hop join)
Show customer name and total number of products they purchased
🧠 Hard 7
Find customers who placed more than 5 orders
🧠 Hard 8
Show categories that have no products
🧠 Hard 9
Show total revenue generated by each department in descending order
🧠 Hard 10 (VERY HARD)
Find the customer who spent the highest amount overall# ai-nl-to-sql-analytics-platform
