import pandas as pd
from datetime import datetime

EXCEL_FILE = "expenses.xlsx"


def add_expense(amount: float, category: str, description: str):

    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame(columns=["Date","Amount","Category","Description"])

    new_row = {
        "Date": datetime.now(),
        "Amount": amount,
        "Category": category,
        "Description": description
    }

    df = pd.concat([df, pd.DataFrame([new_row])])

    df.to_excel(EXCEL_FILE, index=False)

    return "Expense saved"


def get_month_total():

    df = pd.read_excel(EXCEL_FILE)

    total = df["Amount"].sum()

    return f"Total dépenses : {total}"


def get_summary():

    df = pd.read_excel(EXCEL_FILE)

    summary = df.groupby("Category")["Amount"].sum()

    return summary.to_string()