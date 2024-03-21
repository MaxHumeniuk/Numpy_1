import requests
import json

def print_data(data: dict) -> None:
    for k, v in data.items():
        print(f"{k} => {v}")

response = requests.get("https://www.boredapi.com/api/activity")
data = json.loads(response.text)

print_data(data)