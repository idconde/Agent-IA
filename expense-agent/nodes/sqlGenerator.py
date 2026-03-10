from openai import OpenAI
from agentState import AgentState
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()


def generate_sql(state: AgentState):

    prompt = f"""
You are a PostgreSQL expert.

Database schema:

expenses(
    id,
    date,
    amount,
    category,
    description
)

The user intent (e.g. add_expense, get_expenses, get_expenses_by_category, etc.)
is provided separately, but you must also look at the actual message to fill
in details such as amounts, dates, categories and descriptions.

User intent:
{state["user_intent"]}

User request:
{state["message"]}

Generate a SQL query that implements the user's request. For "add_expense"
queries, use the current date when appropriate and properly quote strings.

Return **only the SQL query** without any markdown formatting, code blocks,
or extra commentary. Make sure the query matches the message exactly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sql = response.choices[0].message.content

    # Clean the SQL by removing markdown code blocks
    sql = sql.strip()
    if sql.startswith("```sql"):
        sql = sql[6:]
    if sql.startswith("```"):
        sql = sql[3:]
    if sql.endswith("```"):
        sql = sql[:-3]
    sql = sql.strip()

    state["sql_query"] = sql
    print("Generated SQL:", sql)

    return state