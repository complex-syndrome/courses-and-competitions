import requests
import json
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    if sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

    # api_key already deleted
    link = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=7bff1476a7a992ed55a5e3a4dc385ee5d892118a5f22e9ac81b4ea721a8c79f7"

    response = requests.get(link)
    response.raise_for_status()

    data = response.json()
    print(f"${float(data["data"]["priceUsd"]) * float(sys.argv[1]):,.4f}")

except requests.RequestException:
    sys.exit()
