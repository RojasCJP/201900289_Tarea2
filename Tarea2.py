import json

with open('JSONfile.json') as f:
    data = json.load(f)

for person in data['people']:
    print(person['nombre'], person['apellido'], person['edad'], person['estado'], sep=", ")
