import requests

#API KEY de mi cuenta(tira 200ok): reqres_b051f5730fb6412998dc75c3079ddb08
#API KEY gratuita (tira codigo error 401): reqres-free-v1

HEADER = {"x-api-key": "reqres_b051f5730fb6412998dc75c3079ddb08"}
URL = "https://reqres.in/api/users" #tbm conocida como endpoint
PAYLOAD = {
    "name":"Alan",
    "job":"Piloto"
    }

response = requests.post(URL, headers=HEADER, json=PAYLOAD)

print("Ejecutando request post...")
print("Codigo HTTP:", response.status_code)
print("Objeto posteado en json:")
print(response.json())