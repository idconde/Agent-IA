from openai import OpenAI
from agentState import AgentState
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def send_message(state: AgentState):

    prompt = f"""
You are a helpful assistant that sends messages to the user.

Generate a message to the user based on the result of the SQL query and the original message.
If the SQL query result is empty, it means there are no expenses matching the user's request. 
In this case, generate a message informing the user that no expenses were found.
You should take into account the intent of the user.
You should take into account the sql query that was generated.
The amount should be formatted with 2 decimal places and the euro symbol, for example: "20.00 €".

The message should be concise and short, ideally one or two sentences at most.
User request:
{state["message"]}
SQL query result:
{state["result"]}
User intent:
{state["user_intent"]}
SQL query:
{state["sql_query"]}
"""  
    response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": prompt}
        ]
    )

    response_message = response.choices[0].message.content
    state["response_message"] = response_message
    return state
