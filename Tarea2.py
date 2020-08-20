import json
from xml.dom import minidom;

# aqui empieza el proceso para archivo json

# se abre el archivo json y se lee
with open('JSONfile.json') as f:
    data = json.load(f)

# se muestra el archivo json en consola y de una manera legible
print("json file down")
print()
for person in data['people']:
    print(person['nombre'], person['apellido'], person['edad'], person['estado'], sep = ", ")

# aqui empieza el proceso para archivo xml
# se parsea el archivo xml a python
dataXml = minidom.parse("XMLfile.xml");

# se agregan los datos del archivo xml a un arreglo con cada campo
clave = [dataXml.getElementsByTagName("clave")[0], dataXml.getElementsByTagName("clave")[1], dataXml.getElementsByTagName("clave")[2], dataXml.getElementsByTagName("clave")[3]]
nombre = [dataXml.getElementsByTagName("nombre")[0], dataXml.getElementsByTagName("nombre")[1], dataXml.getElementsByTagName("nombre")[2], dataXml.getElementsByTagName("nombre")[3]]
apellido = [dataXml.getElementsByTagName("apellido")[0], dataXml.getElementsByTagName("apellido")[1], dataXml.getElementsByTagName("apellido")[2], dataXml.getElementsByTagName("apellido")[3]]
carnet = [dataXml.getElementsByTagName("carnet")[0], dataXml.getElementsByTagName("carnet")[1], dataXml.getElementsByTagName("carnet")[2], dataXml.getElementsByTagName("carnet")[3]]

# se muestran en consola los campos del archivo xml
print()
print()
print("xml file down")
print()
print(clave[0].firstChild.data, nombre[0].firstChild.data, apellido[0].firstChild.data, carnet[0].firstChild.data, sep = ", ")
print(clave[1].firstChild.data, nombre[1].firstChild.data, apellido[1].firstChild.data, carnet[1].firstChild.data, sep = ", ")
print(clave[2].firstChild.data, nombre[2].firstChild.data, apellido[2].firstChild.data, carnet[2].firstChild.data, sep = ", ")
print(clave[3].firstChild.data, nombre[3].firstChild.data, apellido[3].firstChild.data, carnet[3].firstChild.data, sep = ", ")
