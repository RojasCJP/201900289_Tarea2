import json
from xml.dom import minidom

# aqui empieza el proceso para archivo json

# se abre el archivo json y se lee
with open('JSONfile.json') as f:
    dataJson = json.load(f)

# se muestra el archivo json en consola y de una manera legible
print("json file down")
print(type(dataJson['people']))
registroJsonNo = 1
for person in dataJson['people']:
    print("registro " + str(registroJsonNo))
    print(person['nombre'], person['apellido'], person['edad'], person['estado'], sep=", ")
    registroJsonNo += 1

# aqui empieza el proceso para archivo xml
# se parsea el archivo xml a python
dataXml = minidom.parse("XMLfile.xml");

# se muestran en consola los campos del archivo xml
print()
print()
print("xml file down")
print(type(dataXml.getElementsByTagName("estudiantes")))
estudianteNo = 0
#se agregan a cada variable un campo de el archivo xml y luego se imprime para que tenga sierto formato
while estudianteNo <= 3:
    clave = dataXml.getElementsByTagName("clave")[estudianteNo]
    nombre = dataXml.getElementsByTagName("nombre")[estudianteNo]
    apellido = dataXml.getElementsByTagName("apellido")[estudianteNo]
    carnet = dataXml.getElementsByTagName("carnet")[estudianteNo]
    print("registro " + str(estudianteNo + 1))
    print(clave.firstChild.data, nombre.firstChild.data, apellido.firstChild.data, carnet.firstChild.data, sep=", ")
    estudianteNo += 1

