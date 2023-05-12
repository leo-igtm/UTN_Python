'''
Leonardo Figueroa div f
1) Listar por pantalla los juegos cuyo género no contenga la palabra
 “pelea”.

2) Calcular y mostrar la cantidad de juegos de una década determinada,
la misma será ingresada por el usuario por pantalla.

3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de
manera ascendente (‘asc’) o descendente („desc‟).

4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan
dicha búsqueda. (Usando RegEx).

5) Exportar a CSV la lista de juegos según opción 1 o 3.

6) Salir.
'''

import json
import re 
import csv

def parse_json_stark(nombre_archivo:str)->list:
    '''Abre un archivo, en modo lectura y lo carga en un diccionario para luego retornarlo'''
    dic_json = {}

    archivo = open(nombre_archivo,"r")
    dic_json = json.load(archivo)
    archivo.close() 
    return dic_json["juegos"]

lista_juegos = parse_json_stark("Parcial\\data_pp.json")

def esNumero(texto:str):
    while True:
        valor = input(texto)
        if re.match('^\d+$',valor):
            return int(valor)
        else:
            print("Por favor ingresar una opcion valida: ") 

def listar_juego_genero(lista_juegos:list,palabra_ingresada:list):

    lista_aux_juego = []

    for juego in lista_juegos:
        genero = juego["genero"]
        contiene_palabra = False
        for palabra in palabra_ingresada:
            if palabra in genero:
                contiene_palabra = True
                break
        if not contiene_palabra:
            lista_aux_juego.append(juego)            
            print(juego["nombre"] + "(" + juego["genero"] + ") ","\n")
    return

def calular_cantidad_juegos(juegos:list,cantidad:int):

    if cantidad >= len(juegos):   
        lista_aux_juegos = []        
        for indice in range(cantidad):
            lista_aux_juegos.append(juegos[indice]["nombre"] + '[' + str(juegos[indice]["anio"]) + ']')
        resultado = lista_aux_juegos
        print("Valor ingresado supera la lista , se mostrara los primeros juegos: \n",resultado,"\n")
    else:
        lista_aux_juegos = []        
        for indice in range(cantidad):
            lista_aux_juegos.append(juegos[indice]["nombre"] + '[' + str(juegos[indice]["anio"]) + ']')
        resultado = lista_aux_juegos 
        print("Se mostrara los primeros juegos: \n",resultado,"\n")
  
    return resultado


def mostrar_menu_opciones():
    
    print("\t1. Listar los juegos segun genero")
    print("\t2. Calcular y mostrar la cantidad de juegos segun década ")
    print("\t3. Listar los juegos ordenados por Empresa")
    print("\t4. Buscar juegos por modo [multijugador, cooperativo]")
    print("\t5. Exportar a CSV la lista de juegos según opción 1 o 3")
    print("\t6. SALIR")

    opcion=esNumero("Elija una opcion: ")
    return opcion

def opciones():
    continuar = True
    while continuar:
        opcion = mostrar_menu_opciones()
        match opcion:
            case 1:
                #palabra_excluida = ["Pelea"]
                listar_juego_genero(lista_juegos,["Accion"])
                break
            case 2:
                calular_cantidad_juegos(lista_juegos,esNumero("Ingresar cantidad de juegos: "))
                break
    return opcion

opciones()