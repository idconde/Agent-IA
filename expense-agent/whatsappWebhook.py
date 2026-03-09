from fastapi import FastAPI, Form
from fastapi.responses import Response
from graph import graph

app = FastAPI()


@app.get("/")
def root():
    return {"status": "agent running"}


@app.post("/whatsapp")
async def whatsapp_webhook(Body: str = Form(...)):

    print("Message reçu :", Body)

    state = {
        "message": Body
    }

    result = graph.invoke(state)

    response = """
<Response>
<Message>Message reçu et traité ✅</Message>
</Response>
"""

    return Response(content=response, media_type="application/xml")