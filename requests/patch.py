import requests
import json

#API KEY de mi cuenta: reqres_b051f5730fb6412998dc75c3079ddb08
#API KEY gratuita (tira codigo error 401): reqres-free-v1

HEADER = {"x-api-key": "reqres_b051f5730fb6412998dc75c3079ddb08"}
URL = "https://reqres.in/api/users/2" #tbm conocida como endpoint
PAYLOAD = {
    "name":"Dani"    
    }

response = requests.patch(URL, headers=HEADER, json=PAYLOAD)    #Cambia parcialmente un registro

print(response.status_code)

data = response.json()
print("Respuesta...")
print(json.dumps(data, indent=2, ensure_ascii=False)) #le da formato al json