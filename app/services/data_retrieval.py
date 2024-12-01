import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

def fetch_stock_data(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}
