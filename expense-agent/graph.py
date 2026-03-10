from langgraph.graph import StateGraph, END

from agentState import AgentState
from nodes.sqlGenerator import generate_sql
from nodes.sqlExecutor import execute_sql
from nodes.messageSender import send_message
from nodes.getUserIntent import get_user_intent


workflow = StateGraph(AgentState)

workflow.add_node("get_user_intent", get_user_intent)
workflow.add_node("generate_sql", generate_sql)
workflow.add_node("execute_sql", execute_sql)
workflow.add_node("send_message", send_message)

workflow.set_entry_point("get_user_intent")

workflow.add_edge("get_user_intent", "generate_sql")
workflow.add_edge("generate_sql", "execute_sql")

workflow.add_edge("execute_sql", "send_message")

workflow.add_edge("send_message", END)

graph = workflow.compile()