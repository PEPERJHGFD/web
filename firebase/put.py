import requests
import json

# Especifica la clave del recurso en la URL
URI = "https://perla-10493-default-rtdb.firebaseio.com/personas/002.json"

# PUT data
data = {
    "nombre": "John Carter",
    "telefono": "1223345636"
}
response = requests.put(URI, json=data)
print(f"DATA: {data}")
print(f"HTTP STATUS: {response.status_code}")
print(f"RESPONSE: {response.text}")
