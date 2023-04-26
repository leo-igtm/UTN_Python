import json
import re

def parse_json_stark(nombre_archivo:str)->list:
    dic_json = {}

    archivo = open(nombre_archivo,"r")
    dic_json = json.load(archivo)
    archivo.close() 
    return dic_json["heroes"]

lista_heroe = parse_json_stark("Ejercicio_stark_archivo\\data_stark.json")
print(f"{lista_heroe}")