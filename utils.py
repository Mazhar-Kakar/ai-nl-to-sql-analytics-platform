from llm import ask_llm # import ask_llm function from llm.py
from prompt import get_prompt # get prompt template from prompt.py

# clean generated sql query
def clean_sql(sql):
    return sql.replace("```", "").replace("sql", "").strip()

def generate_sql(question):
    prompt = get_prompt(question)
    raw_sql = ask_llm(prompt)
    return clean_sql(raw_sql)