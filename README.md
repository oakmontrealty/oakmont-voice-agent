# Oakmont Voice Agent

This repository contains configuration files and instructions for deploying a self‑hosted AI voice agent for Oakmont Realty using LiveKit Agents, ElevenLabs TTS, Deepgram STT and OpenAI for call logic.

## Getting Started

1. Fork or clone this repository to your local machine.
2. Copy `.env.example` to `.env` and fill in the environment variables with your own keys and identifiers.
3. Deploy the container to Google Cloud Run (or another container host) following the deployment instructions.
4. Configure your Twilio SIP trunk to point to the Cloud Run service URL.

## Environment Variables

See `.env.example` for a list of required environment variables. **Never commit your real API keys or secrets to this repository.**

## License

This project is provided as‑is without any warranty.
