import mysql.connector

def run_query(query):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="DB_PASSWORD",
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

    except Exception as e:
        return str(e)