import requests
import json

URI= "https://perla-10493-default-rtdb.firebaseio.com/personas.json"

#PUT data
data = {
    
        "nombre": "John Carter",
        "telefono": "1223345636"
    
}
response = requests.post(URI,json=data)
print(f"DATA: {data}")
print(f"HTTP STATUS:{response}")
print(f"RESPONSE: {response.text}")