from openai import OpenAI
from agentState import AgentState
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def get_user_intent(state: AgentState):

    prompt = f"""
You are a helpful assistant that gets the user intent.
Users will send you messages about their expenses and you need to determine their intent.
Example intents include: "add_expense", "get_expenses", "get_expenses_by_category", "get_expenses_by_date", etc.
Here are the list of categories you should use for expenses:
Food
Transport
Housing
Utilities
Health
Entertainment
Shopping
Education
Travel
Salary
Bills
Insurance
Savings
Taxes
Gifts
Subscriptions
Family
Business
Other

Sometimes user may not clarly state their intent, they may just send messages like :
- "I spent 20 euros on lunch today" (intent: add_expense, category: Food)
- "How much did I spend on groceries last month?" (intent: get_expenses, category: Food)
- "10 euros for Kebab" (intent: add_expense, category: Food)
- "15 euros Taxi" (intent: add_expense, category: Transport)
- "10 euros" (intent: add_expense, category: Other)
- "30" (intent: add_expense, category: Other)
- "69 € Marseille" (intent: add_expense, category: Travel)
- "What did I spend on food last week?" (intent: get_expenses_by_category, category: Food)
- "How much did I spend yesterday?" (intent: get_expenses_by_date)
- "Total" (intent: get_expenses)

Determine the user's intent based on their message.
User request:
{state["message"]}

"""  
    response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": prompt}
        ]
    )

    user_intent = response.choices[0].message.content
    state["user_intent"] = user_intent
    print("Generated user intent:", user_intent)
    return state

