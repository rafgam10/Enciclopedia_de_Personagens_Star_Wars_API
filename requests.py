import requests

#https://swapi.dev/api/

requisicao = requests.get("https://swapi.dev/api/people/1")



print(requisicao.status_code)
