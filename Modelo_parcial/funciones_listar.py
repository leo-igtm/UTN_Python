from Funciones_archivos import parse_json_stark
import json 

lista_heroe = parse_json_stark("Modelo_parcial/data_stark.json")

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