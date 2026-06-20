from langchain_ollama import OllamaLLM
import sqlite3

# Initialize LLM
llm = OllamaLLM(
    model="phi3",
    temperature=0
)

def generate_sql(query):
    prompt = f"""
    You are a SQL expert.

    Convert the following natural language question into a valid SQLite SQL query.
    Return ONLY raw SQL. No explanation, no markdown, no ```.

    Table: sales(product, revenue, region, date)

    Question: {query}
    """

    response = llm.invoke(prompt)

    # 🔥 Clean response
    sql = response.strip()

    # Remove markdown if present
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql

def execute_sql(sql_query):
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"SQL Error: {e}"

def get_answer(query):
    sql = generate_sql(query)
    result = execute_sql(sql)

    return sql, result
