import os
from flask import Flask, request
import google.generativeai as genai
from dotenv import load_dotenv
import database  # This imports the file we created earlier

# 1. Setup
load_dotenv()
app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/incoming-sms', methods=['POST'])
def incoming_sms():
    # Africa's Talking sends data as 'from' and 'text'
    farmer_phone = request.form.get('from')
    raw_text = request.form.get('text')

    # 2. Let Gemini "Think"
    prompt = f"""
    Extract agricultural data from this Kenyan farmer's message: "{raw_text}"
    Return ONLY a JSON object with these keys: 
    crop, qty, unit, location. 
    If data is missing, use "unknown".
    """
    
    response = model.generate_content(prompt)
    # Convert Gemini's text response to a Python Dictionary
    # (In a real app, you'd add error handling here!)
    import json
    extracted_data = json.loads(response.text.strip('`json\n '))
    extracted_data['phone'] = farmer_phone

    # 3. Save to Database
    database.save_harvest(extracted_data)

    # 4. Try to Match with a Buyer
    match = database.find_matching_buyer(extracted_data['crop'], extracted_data['location'])

    if match:
        return f"Match found! Connecting you to buyer at {match['buyer_phone']}", 200
    else:
        return "Harvest listed. We will text you when a buyer is found.", 200

if __name__ == '__main__':
    app.run(port=5000)

