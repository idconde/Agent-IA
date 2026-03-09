from langgraph.graph import StateGraph, END

from agentState import AgentState
from router import router_node
from nodes import (
    parse_expense,
    add_expense,
    get_month_total,
    get_summary
)


workflow = StateGraph(AgentState)

workflow.add_node("router", router_node)

workflow.add_node("parse_expense", parse_expense)
workflow.add_node("add_expense", add_expense)

workflow.add_node("get_month_total", get_month_total)
workflow.add_node("get_summary", get_summary)


workflow.set_entry_point("router")


def route(state: AgentState):

    return state["next_node"]


workflow.add_conditional_edges(
    "router",
    route
)


workflow.add_edge("parse_expense", "add_expense")

workflow.add_edge("add_expense", END)
workflow.add_edge("get_month_total", END)
workflow.add_edge("get_summary", END)

graph = workflow.compile()