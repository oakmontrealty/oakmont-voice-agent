from fastapi import FastAPI, Request, Response
from twilio.twiml.voice_response import VoiceResponse
import os

# Initialize FastAPI app
app = FastAPI()

@app.post("/", response_class=Response, responses={200: {"content": {"application/xml": {}}}})
async def handle_call(request: Request):
    """
    Handle incoming voice calls from Twilio and respond with TwiML.
    Twilio will make a POST request to this endpoint when a call comes in.
    """
    resp = VoiceResponse()
    # Greeting message using Australian English Polly voice. Adjust as needed.
    greeting = (
        "Good morning, you've reached Oakmont Realty. This is the AI assistant for Terrence. "
        "How can I help you today?"
    )
    resp.say(greeting, voice="Polly.Nicole", language="en-AU")
    return Response(content=str(resp), media_type="application/xml")


@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Oakmont voice agent container is running"}
