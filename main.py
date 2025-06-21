from fastapi import FastAPI, Form
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "OK", "message": "Twilio voice bot server running."}

@app.post("/message")
async def message_response(
    From: str = Form(...),
    Body: str = Form(...)
):
    print(f"Incoming message from {From}: {Body}")

    ai_response = "Hi there, this is your AI assistant. I received your message."

    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{ai_response}</Message>
</Response>"""

    return Response(content=twiml, media_type="application/xml")

@app.post("/voice")
async def voice_response():
    ai_response = "Hello Mike, hello Rijul. Looks like I have got it working to some extent."

    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Joanna">{ai_response}</Say>
</Response>"""

    return Response(content=twiml, media_type="application/xml")
