from typing import TypedDict


class AgentState(TypedDict):

    message: str

    next_node: str | None

    amount: float | None
    category: str | None
    description: str | None