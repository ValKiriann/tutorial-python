# importamos requests
import requests
# cogemos datos desde una url en un requests
response = requests.get("https://api.taiga.io/api/v1/projects")
# imprimimos response para ver que ha hecho (si devuelve 200 significa ok)
print (response)
