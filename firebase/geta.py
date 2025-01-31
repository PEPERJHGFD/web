import requests
import json

URI= "https://perla-10493-default-rtdb.firebaseio.com/personas/001.json"

#GET data
response = requests.get(URI)

print(f"HTTP STATUS: {response}")
print(f"RESPONSE: {response.text}")