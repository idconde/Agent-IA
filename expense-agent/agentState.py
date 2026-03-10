from typing import TypedDict


class AgentState(TypedDict):

    message: str

    sql_query: str | None

    result: list | None

    response_message: str | None

    user_intent: str | None