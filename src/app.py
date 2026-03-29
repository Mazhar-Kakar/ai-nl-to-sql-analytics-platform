import streamlit as st
import pandas as pd
from utils import generate_sql
from db import run_query

# UI CODE 
# ======================================================================
st.title("NL → SQL App") # app heading

# Questions Suggestions Sidebar
st.sidebar.title("Sample Questions")

st.sidebar.button("Show databases")
st.sidebar.button("Show tables")
st.sidebar.button("Show all customers")
st.sidebar.button("Show top 10 customers")
st.sidebar.button("show me how many products never ordered")
st.sidebar.button("total orders per customer")
st.sidebar.button("total sales by department")

question = st.text_input("Ask your question:")

# Run - send question to llm model
if st.button("Run"):
    if question:

        sql_query = generate_sql(question) # send NL question to llm

        st.subheader("Generated SQL") # show generated sql query from qwen2.5:3b llm model
        st.code(sql_query)

        result = run_query(sql_query) # run query and show result 

        if isinstance(result, str):
            st.error(result)
        else:
            columns, rows = result
            df = pd.DataFrame(rows, columns=columns)
            st.dataframe(df)