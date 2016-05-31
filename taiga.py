# importamos requests
import csv
import requests
def get_activity(x):
    return x['total_activity']
# cogemos datos desde una url en un requests (?page_size=20 nos ayuda a que sea más rápido cogiendo 20)
response = requests.get("https://api.taiga.io/api/v1/projects?page_size=20")
# imprimimos response para ver que ha hecho (si devuelve 200 significa ok)
# print (response)
# le decimos que projects es el json de response
projects = response.json()
# print(projects)
# print(len(projects))
# para crear una lista vacia
result = []
# creamos proyectos
for project in projects:
    result.append({
        'id': project['id'],
        'name': project['name'],
        'description': project['description'],
        'owner': project['owner']['full_name_display'],
        'total_activity': project['total_activity']
    })

result.sort(key=get_activity, reverse=True)
# abrimos el archivo csv y lo escribimos con el array de la api
with open('projects.csv', 'w') as csvfile:
    fieldnames = ['total_activity', 'id', 'name', 'description', 'owner']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    for r in result:
        writer.writerow(r)
