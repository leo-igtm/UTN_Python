import json

def parse_json_stark(nombre_archivo:str)->list:
    '''Abre un archivo, en modo lectura y lo carga en un diccionario para luego retornarlo'''
    dic_json = {}

    archivo = open(nombre_archivo,"r")
    dic_json = json.load(archivo)
    archivo.close() 
    return dic_json["heroes"]

lista_heroe = parse_json_stark("Modelo_parcial/data_stark.json")