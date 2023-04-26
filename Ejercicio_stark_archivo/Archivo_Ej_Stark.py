import json
import re
import csv

def parse_json_stark(nombre_archivo:str)->list:
    dic_json = {}

    archivo = open(nombre_archivo,"r")
    dic_json = json.load(archivo)
    archivo.close() 
    return dic_json["heroes"]

lista_heroe = parse_json_stark("Ejercicio_stark_archivo\\data_stark.json")
print(f"{lista_heroe}")


def guardar_csv_stark(nombre_archivo:str,lista:list):
    
    archivo = open(nombre_archivo,"w")
    for heroe in lista:
        linea = heroe["nombre"] + "," + heroe["identidad"] + "," + heroe["empresa"] + "," + str(heroe["altura"]) + "," + str(heroe["peso"]) + "," + heroe["genero"] + "," + heroe["color_ojos"] + "," + heroe["color_pelo"] + "," + str(heroe["fuerza"]) + "," + heroe["inteligencia"] + "\n"
        archivo.write(linea)
    archivo.close()
    

guardar_csv_stark("Ejercicio_stark_archivo\data_stark.csv",lista_heroe)