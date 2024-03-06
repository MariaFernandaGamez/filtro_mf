import os
import json
BASE_DATA="CuartoEjer/data/"
ruta="CuartoEjer/data/Empleados.json"

def Checkfile(Archivo,diccionario):
    if(not(os.path.isfile(BASE_DATA+Archivo))):
        with open (BASE_DATA+Archivo,"w+") as CreateFile:
            json.dump(diccionario, CreateFile, indent=4)

def UpdateFile(Archivo,diccionario):
    with open(Archivo,"w+") as WriteFile:
        json.dump(diccionario, WriteFile, indent=4)

def ReadFile(Archivo):
    with open(BASE_DATA+Archivo,"r") as ReadFile:
        return json.loads(ReadFile.read())