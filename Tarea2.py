import json
from xml.dom import minidom
import csv


# aqui empieza el proceso para archivo json
# se abre el archivo json y se lee


def leerJson():
    with open('JSONfile.json') as f:
        dataJson = json.load(f)
    # se muestra el archivo json en consola y de una manera legible
    print("------------------------------------------------------------------")
    print("------------------------JSON FILE---------------------------------")
    print("------------------------------------------------------------------")
    print(type(dataJson['people']))
    registroJsonNo = 1
    for person in dataJson['people']:
        print("registro " + str(registroJsonNo)+" "+person['nombre'], person['apellido'], person['edad'], person['estado'], sep=", ")
        registroJsonNo += 1


def leerXml():
    # se parsea el archivo xml a python
    dataXml = minidom.parse("XMLfile.xml");
    # se muestran en consola los campos del archivo xml
    print()
    print()
    print("------------------------------------------------------------------")
    print("------------------------XML FILE----------------------------------")
    print("------------------------------------------------------------------")
    print(type(dataXml.getElementsByTagName("estudiantes")))
    estudianteNo = 0
    # se agregan a cada variable un campo de el archivo xml y luego se imprime para que tenga sierto formato
    while estudianteNo <= 3:
        clave = dataXml.getElementsByTagName("clave")[estudianteNo]
        nombre = dataXml.getElementsByTagName("nombre")[estudianteNo]
        apellido = dataXml.getElementsByTagName("apellido")[estudianteNo]
        carnet = dataXml.getElementsByTagName("carnet")[estudianteNo]
        print("registro " + str(estudianteNo + 1) +" "+ clave.firstChild.data, nombre.firstChild.data, apellido.firstChild.data, carnet.firstChild.data, sep=", ")
        estudianteNo += 1


def leerCsv():
    print()
    print()
    print("------------------------------------------------------------------")
    print("------------------------CSV FILE----------------------------------")
    print("------------------------------------------------------------------")
    usuarioNo = 1
    # cargo el archivo para python
    with open('CSVfile.csv') as f:
        dataCsv = csv.reader(f)
        print(type(dataCsv))
        for row in dataCsv:
            print("registro " + str(usuarioNo) + " {0}, {1}, {2}, {3}".format(row[0], row[1], row[2], row[3]))
            usuarioNo += 1


leerJson()
leerXml()
leerCsv()
