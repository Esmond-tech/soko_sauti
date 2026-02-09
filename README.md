# soko_sauti
An AI-powered voice and SMS marketplace connecting offline small-scale Kenyan farmers to real-time buyers using Gemini 1.5 and Africa's Talking.
# Soko-Sauti 
**Bridging the Digital Divide for Kenyan Small-Scale Farmers**

## The Vision
Soko-Sauti (Voice Market) is an AI-driven platform designed for the millions of Kenyan farmers who use basic feature phones. By leveraging **Gemini 1.5 Flash** and **Africa's Talking**, we turn simple voice calls into structured market data, connecting rural harvests to urban demand instantly.

## Tech Stack
* **Brain:** Google Gemini 1.5 Flash (NLP & Translation)
* **Connectivity:** Africa's Talking (Voice/SMS/USSD)
* **Payments:** Safaricom Daraja API (M-Pesa Escrow)
* **Database:** MongoDB Atlas
* **Backend:** Python (FastAPI/Flask)

## How it Works
1. **The Call:** A farmer calls a local number and speaks their harvest details in English or Swahili.
2. **The Extraction:** Gemini processes the audio/text to extract crop type, quantity, and location.
3. **The Match:** The system queries the database for buyers looking for that specific produce.
4. **The Transaction:** An SMS is sent to both parties, and payment is secured via M-Pesa Escrow.

## Project Structure
- `app.py`: Main API and logic handler.
- `database.py`: MongoDB connection and matching queries.
- `requirements.txt`: Python dependencies.
- `.env`: (Hidden) API keys and credentials.

---
*Developed by Carlos - Software Engineering Student at Kisii University.*
