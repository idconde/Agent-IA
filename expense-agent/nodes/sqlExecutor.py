from db.database import get_connection


def execute_sql(state):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(state["sql_query"])

    # Check if this is a SELECT query (which returns results)
    sql_upper = state["sql_query"].strip().upper()
    if sql_upper.startswith("SELECT"):
        rows = cursor.fetchall()
        state["result"] = rows
    else:
        # For INSERT, UPDATE, DELETE queries, commit the transaction
        conn.commit()
        state["result"] = "Query executed successfully"

    conn.close()
    print(state)

    return state