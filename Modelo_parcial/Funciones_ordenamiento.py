from Funciones_archivos import parse_json_stark 

lista_heroe = parse_json_stark("Modelo_parcial/data_stark.json")

# 2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
# # manera ascendente (‘asc’) o descendente (‘desc’)

def ordenar_heroe_altura(lista_heroe:list,asc:str) -> list:
    

    ordenada = True
    bandera_swap = True
    for i in range(len(lista_heroe)-1):
        if lista_heroe[i]["altura"] > lista_heroe[i+1]["altura"]:
            ordenada == False
            break
    lista_auxiliar = []
    if not ordenada:
        while bandera_swap == True:
            bandera_swap = False
            for i in range(len(lista_heroe)-1):
                if asc == 'asc' or lista_heroe[i]["altura"] > lista_heroe[i+1]["altura"]:        
                    aux = lista_heroe[i]
                    lista_heroe[i] = lista_heroe[i+1]
                    lista_heroe[i+1] = aux
                    lista_auxiliar.append(lista_heroe[i]["nombre"] + '[' + str(lista_heroe[i]["altura"]) + '] ')
                bandera_swap = True
                print("Lista ordenada",lista_auxiliar)

    return lista_heroe

ordenar_heroe_altura(lista_heroe,'asc')

def ordenar_heroe_fuerza(lista_heroe:list,asc:str):
    bandera_swap = True
    while bandera_swap == True:
        bandera_swap = False
        for i in range(len(lista_heroe)-1):
            if asc == 'asc' or (lista_heroe[i]["fuerza"] > lista_heroe[i+1]["fuerza"]):
                aux = lista_heroe[i]
                lista_heroe[i] = lista_heroe[i+1]
                lista_heroe[i+1] = aux
                bandera_swap = True
            
    lista_auxiliar = []
    for heroe in lista_heroe:
        lista_auxiliar.append(heroe["nombre"] + '[' + str(heroe["fuerza"]) + '] ')
    print("Lista ordenada",lista_heroe)
    
    return

ordenar_heroe_altura(lista_heroe,'asc')
