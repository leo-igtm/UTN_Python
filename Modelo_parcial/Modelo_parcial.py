#1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
# (Validar que no supere max. de lista)

# 2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
# manera ascendente (‘asc’) o descendente (‘desc’)

# 3. Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar
# de manera ascendente (‘asc’) o descendente (‘desc’)

# 4. Calcular promedio de cualquier key numérica, filtrar los que cumplan con la
# condición de superar o no el promedio (preguntar al usuario la condición:
# ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser
# mayores o menores según corresponda.

# 5. Buscar héroes por inteligencia [good, average, high] y listar en consola los
# que cumplan dicha búsqueda. (Usando RegEx)

# 6. Exportar a CSV la lista de héroes ordenada según opción elegida
# anteriormente [1-4]

# Aclaraciones:
# ● Los puntos deben ser accedidos mediante un menú. Para todas las opciones,
# validar lo ingresado por consola con RegEx
# ● El set de datos proviene de un json
# ● Realizar las validaciones que crea pertinentes
# ● En todos los casos se deberá trabajar con una copia de la lista original

import json
import re
import csv

def parse_json_stark(nombre_archivo:str)->list:
    '''Abre un archivo, en modo lectura y lo carga en un diccionario para luego retornarlo'''
    dic_json = {}

    archivo = open(nombre_archivo,"r")
    dic_json = json.load(archivo)
    archivo.close() 
    return dic_json["heroes"]

lista_heroe = parse_json_stark("Ejercicio_stark_archivo\\data_stark.json")


def listar_cantidad_heroe(cantidad:int,heroes:list):
    '''Muestra la cantidad de heroes , si el numero ingresado supera la lista mostrara todos los heroes,
      caso contrario que el numero sea menor a la lista, mostrara los primeros heroes, y retornara su resultado '''
    if cantidad >= len(heroes):   
        lista_aux_heroe = []        
        for indice in range(cantidad):
            heroe = heroes[indice]["nombre"]
            lista_aux_heroe.append(heroe)
            resultado = lista_aux_heroe
            print("Valor ingresado supera la lista , se mostrara los primeros heroes: ",heroe)
    else:
        lista_aux_heroe = []        
        for indice in range(cantidad):
            heroe = heroes[indice]["nombre"]
            lista_aux_heroe.append(heroe)
            print("Se mostrara los primeros heroes: ",heroe)
            resultado = False
    return resultado

listar_cantidad_heroe(22,lista_heroe)

# 2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
# # manera ascendente (‘asc’) o descendente (‘desc’)

def ordenar_heroe_altura(lista_heroe:list,asc:str) -> list:
    
    lista_auxiliar = []

    ordenada = True
    bandera_swap = True
    for i in range(len(lista_heroe)-1):
        if lista_heroe[i]["altura"] > lista_heroe[i+1]["altura"]:
            ordenada == False
            break
        
    if not ordenada:
        while bandera_swap == True:
            bandera_swap = False
            for i in range(len(lista_heroe)-1):
                if asc == 'asc' or lista_heroe[i]["altura"] > lista_heroe[i+1]["altura"]:        
                    aux = lista_heroe[i]
                    lista_heroe[i] = lista_heroe[i+1]
                    lista_heroe[i+1] = aux
                    lista_auxiliar.append(lista_heroe[i]["nombre"] + '[' + str(lista_heroe[i]["altura"]) + '] ')
                print("Lista ordenada",lista_auxiliar)

                bandera_swap = True

    return lista_heroe

ordenar_heroe_altura(lista_heroe,'asc')

# def ordenar_heroe_fuerza(lista_heroe:list,asc:str):
#     bandera_swap = True
#     while bandera_swap == True:
#         bandera_swap = False
#         for i in range(len(lista_heroe)-1):
#             if asc == 'asc' or (lista_heroe[i]["fuerza"] > lista_heroe[i+1]["fuerza"]):
#                 aux = lista_heroe[i]
#                 lista_heroe[i] = lista_heroe[i+1]
#                 lista_heroe[i+1] = aux
#                 bandera_swap = True
            
#     lista_auxiliar = []
#     for heroe in lista_heroe:
#         lista_auxiliar.append(heroe["nombre"] + '[' + str(heroe["fuerza"]) + '] ')
#     print("Lista ordenada",lista_heroe)
    
#     return

# ordenar_heroe_altura(lista_heroe,'asc')

# def mostrar_menu_opciones():
    
#     print("Listar los primeros Heroes")
#     print("Ordenar y listar heroes por altura")
#     print("Ordenar y listar heroes por fuerza")
#     print("Calcular promedio")
#     print("Buscar y listar heroe por inteligencia")
#     print("Exportar a csv")

# def ingreso_opciones():
    
#     for opcion in mostrar_menu_opciones():
#         opcion = input("Ingrese una opcion: ")
#         print(opcion)
    
# def opciones():
#     opcion = mostrar_menu_opciones() 
#     continuar = True
#     while continuar:
#         opcion = ingreso_opciones(opcion)
#         match opcion:
#             case 1:
#                 listar_cantidad_heroe(13,lista_heroe)
#             #     break
#             # case 2:
#             #     break
#             # case 3:
#             #     break
#             # case 4:
#             #     break
#             # case 5:
#             #     break
#             # case 6:
#                 break
#     return opcion

# opciones()
