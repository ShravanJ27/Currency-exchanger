import requests
import os 
from dotenv import load_dotenv

load_dotenv()

curr = input("What currency would you like to exchange from (Use code): ").upper()
amount = input(f"How much {curr} would you like to exchange? ")

tar_curr = input(f"What would you like to convert {curr} to? ").upper()

API_KEY = os.getenv("EXCHANGERATE_API_KEY")
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{curr}"

response = requests.get(url)
if response.status_code == 200: 
    data = response.json()
    rate = data["conversion_rates"][tar_curr]
    change_rate = float(amount) * float(rate)
    print(f"{amount} {curr} == {change_rate} {tar_curr}")


