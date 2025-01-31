import requests
import json

URI= "https://perla-10493-default-rtdb.firebaseio.com/personas/002.json"

#DELETE data
response = requests.delete(URI)
print(f"RESPONSE: {response.text}")