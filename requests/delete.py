import requests

#API KEY de mi cuenta(tira 200ok): reqres_b051f5730fb6412998dc75c3079ddb08
#API KEY gratuita (tira codigo error 401): reqres-free-v1

HEADER = {"x-api-key": "reqres_b051f5730fb6412998dc75c3079ddb08"}
URL = "https://reqres.in/api/users/2" #tbm conocida como endpoint


response = requests.delete(URL, headers=HEADER)

print("Ejecutando request delete...")
print("Codigo HTTP:", response.status_code) # 204
print("Objeto en json:")
print("Objeto:",response.text) #no va encontrar nada porque el objeto fue borrado