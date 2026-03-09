import json
import pandas as pd
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from agentState import AgentState

client = OpenAI()

EXCEL_FILE = "expenses.xlsx"


def parse_expense(state: AgentState):

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "system",
                "content": """
Extract expense data from the user's message.

Return a valid JSON object with the following keys:
- amount: a number representing the expense amount
- category: a string for the expense category
- description: a string describing the expense

"""
            },
            {
                "role": "user",
                "content": state["message"]
            }
        ]
    )

    content = response.choices[0].message.content.strip()
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {content}")
        raise e

    state["amount"] = data.get("amount", 0)
    state["category"] = data.get("category", "Unknown")
    state["description"] = data.get("description", state["message"])

    return state


def add_expense(state: AgentState):

    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame(columns=["Date","Amount","Category","Description"])

    new_row = {
        "Date": datetime.now(),
        "Amount": state["amount"],
        "Category": state["category"],
        "Description": state["description"]
    }

    df = pd.concat([df, pd.DataFrame([new_row])])

    df.to_excel(EXCEL_FILE, index=False)

    print("Expense saved")

    return state


def get_month_total(state: AgentState):

    df = pd.read_excel(EXCEL_FILE)

    total = df["Amount"].sum()

    print("Total:", total)

    return state


def get_summary(state: AgentState):

    df = pd.read_excel(EXCEL_FILE)

    summary = df.groupby("Category")["Amount"].sum()

    print(summary)

    return state