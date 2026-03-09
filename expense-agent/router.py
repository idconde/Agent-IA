import json
from openai import OpenAI
from agentState import AgentState
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()


def router_node(state: AgentState):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a router.

Choose the next node.

Possible nodes:

parse_expense
get_month_total
get_summary

Return JSON:

next_node
"""
            },
            {
                "role": "user",
                "content": state["message"]
            }
        ]
    )

    result = json.loads(response.choices[0].message.content)


    state["next_node"] = result["next_node"]

    return state