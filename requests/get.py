import requests
import json

import sys
sys.stdout.reconfigure(encoding='utf-8') #para que los emojis no jodan la consola

#API KEY de mi cuenta(tira 200ok): reqres_b051f5730fb6412998dc75c3079ddb08
#API KEY gratuita (tira codigo error 401): reqres-free-v1

HEADER = {"x-api-key": "reqres_b051f5730fb6412998dc75c3079ddb08"}
URL = "https://reqres.in/api/users?page=2" #tbm conocida como endpoint

response = requests.get(URL, headers=HEADER, verify=True)

print("Ejecutando request get...")
print("Codigo HTTP:", response.status_code)

data = response.json()
print("Respuesta...")
print(json.dumps(data, indent=2, ensure_ascii=False)) #le da formato al json