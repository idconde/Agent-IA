from db.database import get_connection


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id SERIAL PRIMARY KEY,
        date TIMESTAMP,
        amount NUMERIC,
        category TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized")