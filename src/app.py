import streamlit as st
import pandas as pd
from backend import run_query, generate_sql

st.title("NL → SQL App") # App Heading

# Sample Questions Sidebar
st.sidebar.title("Sample Questions")
st.sidebar.code("Show databases")
st.sidebar.code("Show tables")
st.sidebar.code("Show all customers")
st.sidebar.code("Show top 10 customers")
st.sidebar.code("Show me total products that never ordered")
st.sidebar.code("Total orders per customer")
st.sidebar.code("Total sales by department")


question = st.text_input("Ask your question:") 


# Run - send question to llm model
if st.button("Run"):
    if question:

        sql_query = generate_sql(question) # Pass NL question to LLM, Store Generated sql query into {sql_query} variable


        st.subheader("Generated SQL") # Display generated SQL query from qwen2.5:3b llm model
        st.code(sql_query)

        result = run_query(sql_query) # Pass Generated Sql query to database query executer function, and store result into {result} variable

        if isinstance(result, str): # If {result} datatype is string then display error.
            st.error(result)
        else:                       # convert result into pandas datafram with column names
            columns, rows = result
            df = pd.DataFrame(rows, columns=columns)
            st.dataframe(df) # display dataframe on streamlit app as result