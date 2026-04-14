import requests

API_KEY = 'fca_live_em802pRQh9kQnffreW0rYATSm6RldkhDwljKhPQn'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

def convert_currency(base):
    url = f"{BASE_URL}&base_currency={base}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    # remove base currency if present
    if base in data:
        del data[base]

    for ticker, value in data.items():
        print(f"{ticker}: {value}")