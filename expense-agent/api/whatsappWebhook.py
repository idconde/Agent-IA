from fastapi import FastAPI, Form
from fastapi.responses import Response
from graph import graph
from db.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"status": "agent running"}


@app.post("/whatsapp")
async def whatsapp_webhook(Body: str = Form(...), From: str = Form(...)):

    print("Message reçu :", Body, "from :", From)

    state = {
        "message": Body
    }

    result = graph.invoke(state)

    response = f"""
<Response>
<Message>{result['response_message']}</Message>
</Response>
"""

    return Response(content=response, media_type="application/xml")