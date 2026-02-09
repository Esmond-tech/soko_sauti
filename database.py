import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

# 1. Load the secrets from your .env file
load_dotenv()

# 2. Get the URI from the environment variable
# Make sure your .env has: MONGO_URI="mongodb+srv://..."
MONGO_URI = os.getenv("MONGO_URI")

# 3. Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.soko_sauti

def save_harvest(farmer_data):
    """
    Saves the AI-extracted data into the Harvests collection
    farmer_data: dictionary from Gemini
    """
    harvest_record = {
        "farmer_phone": farmer_data['phone'],
        "crop": farmer_data['crop'],
        "quantity": farmer_data['qty'],
        "location": farmer_data['location'],
        "status": "available",
        "created_at": datetime.utcnow()
    }
    
    result = db.harvests.insert_one(harvest_record)
    return result.inserted_id

def find_matching_buyer(crop_name, location):
    """
    Looks for a buyer interested in this crop in this area
    """
    query = {
        "crop_requested": crop_name,
        "preferred_location": location,
        "status": "active"
    }
    return db.demands.find_one(query)

