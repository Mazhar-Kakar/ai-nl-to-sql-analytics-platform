import requests
import mysql.connector
from dotenv import load_dotenv
import os
from prompt import get_prompt # import get_prompt function with question and prompt templates from prompt.py

# load environment variables
load_dotenv()

# Call LLM
def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# Clean SQL
def clean_sql(sql): 
    """clean generated sql query, remove unwanted characters and
    remove leading and trailing space"""
    return sql.replace("```", "").replace("sql", "").strip()


# Generate SQL
def generate_sql(question):
    prompt = get_prompt(question)
    raw_sql = ask_llm(prompt)
    return clean_sql(raw_sql) # Pass generated query for cleaning


# Run the query
def run_query(query):
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="sales_db"
        )

        cursor = conn.cursor()              
        cursor.execute(query)

        if query.lower().startswith("select") or query.lower().startswith("show"):
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]  # column names
            result = (columns, rows)
        else:
            conn.commit()
            result = ("message", [("Query executed",)])

        cursor.close()
        conn.close()

        return result