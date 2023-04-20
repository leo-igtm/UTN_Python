#Leonardo Figueroa div f 
#A. Analizar detenidamente el set de datos
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
#F. Recorrer la lista y determinar la altura promedio de los superhéroes(PROMEDIO)
#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
#H .Calcular e informar cual es el superhéroe más y menos pesado.
from data_stark import lista_personajes

heroe_mas_Alto = lista_personajes[0]["altura"]
maximo_altura_superheroe = float(heroe_mas_Alto)
heroe_mas_bajo = lista_personajes[0]["altura"]# Defino la lista en diccionario y lo guardo en una variable
minimo_altura_superheroe = float(heroe_mas_bajo) # Se realiza la conversion de la variable que contiene la lista de diccionarios

heroe_mas_pesado = lista_personajes[0]["peso"]
maximo_peso_superheroe = float(heroe_mas_pesado)

heroe_menos_pesado = lista_personajes[0]["peso"]
menor_peso_superheroe = float(heroe_menos_pesado)


# def mostrar_menu_opciones():
    
#     print("\tBIENVENIDOS A STARK \n")
#     print("1 Mostrar Nombre de cada superhéroe \n"
#     "2 Mostrar Nombre de cada superhéroe y altura \n"
#     "3 Mostrar superhéroe más alto \n"
#     "4 Mostrar superhéroe más bajo \n"
#     "5 Mostrar altura promedio de los superhéroes \n"
#     "6 Mostrar  superhéroe más pesado \n"
#     "7 Mostrar superheroe menos pesado \n"
#     "8 Salir \n") 
    
#     opciones = input("Ingrese una opcion: ")
#     opcion = int(opciones)
#     return opcion

# mostrar_menu_opciones()




    
  




def imprimir_nombre_superheroes():
    for lista in lista_personajes:
        mostrar_lista_superheroes = lista["nombre"]
        print("<-------------------------------------------->")
        print("Personaje: ",mostrar_lista_superheroes)
    return
imprimir_nombre_superheroes()

def imprimir_nombre_altura_superheroes():

    for lista in lista_personajes:
        altura = float(lista["altura"])
        print("<-------------------------------------------->")
        print("Personaje: ",lista["nombre"],"Altura: {0:.2f}".format(altura))
    return

imprimir_nombre_altura_superheroes()

def imprimir_superheroe_mas_alto():
    altura_max_superheroe = lista_personajes[0]["altura"]
    for lista in range(len(lista_personajes)):
        altura_max_superheroe = float(lista_personajes[lista]["altura"])
        if lista == 0 or  altura_max_superheroe > heroe_mas_Alto :
            heroe_mas_Alto = lista_personajes[lista]["altura"]
            nombre_lista_inicial = lista

    print("<-------------------------------------------->")
    print("Personaje: ",nombre_lista_inicial)    
    print("El personaje mas alto:","Altura: {0:.2f} ".format(heroe_mas_Alto))
    return 

imprimir_superheroe_mas_alto()

def imprimir_superheroe_mas_bajo():
    flag_ingreso = False

    for lista in lista_personajes:
        altura_min_superheroe = float(lista["altura"])
        if flag_ingreso == False or altura_min_superheroe < heroe_mas_bajo:
            heroe_mas_bajo = altura_min_superheroe
            nombre_superheroe_bajo = lista["nombre"]
            flag_ingreso = True
    print("Personaje: ",nombre_superheroe_bajo)
    print("El personaje mas bajo: ","{0:.2f} ".format(heroe_mas_bajo))
    return
 
imprimir_superheroe_mas_bajo()


def imprimir_promedio_alturas_superheroes():
    suma_altura_personajes = 0
    for lista in lista_personajes:
        suma_altura_personajes += float((lista["altura"]))
        promedio_altura_personajes = suma_altura_personajes / len(lista)
    print("El promedio es: {0:.2f} ".format(promedio_altura_personajes))
    return

imprimir_promedio_alturas_superheroes()


def imprimir_superheroe_mas_pesado():
    flag_ingreso = False

    for lista in lista_personajes:
        peso_max_superheroe = float(lista["peso"])
        if flag_ingreso == False or peso_max_superheroe > heroe_mas_pesado:
            heroe_mas_pesado = peso_max_superheroe
            nombre_superheroe = lista["nombre"]
            flag_ingreso = True
    print("Personaje: ",nombre_superheroe)
    print("El personaje mas pesado: ","{0:.2f} ".format(heroe_mas_pesado))
    return

imprimir_superheroe_mas_pesado()

def imprimir_superheroe_menos_pesado():
    flag_ingreso = False

    for lista in lista_personajes:
        peso_min_superheroe = float(lista["peso"])
        if flag_ingreso == False or peso_min_superheroe < heroe_menos_pesado:
            heroe_menos_pesado = peso_min_superheroe
            nombre_superheroe = lista["nombre"]
            flag_ingreso = True
    print("Personaje: ",nombre_superheroe)
    print("El personaje menos pesado: ","{0:.2f} ".format(heroe_menos_pesado))
    return

imprimir_superheroe_menos_pesado()

def mostrar_menu_opciones():

    lista_menu =\
    [
        "1 Mostrar Nombre de cada superhéroe ",
        "2 Mostrar Nombre de cada superhéroe y altura ",
        "3 Mostrar superhéroe más alto ",
        "4 Mostrar superhéroe más bajo ",
        "5 Mostrar altura promedio de los superhéroes ",
        "6 Mostrar  superhéroe más pesado ",
        "7 Mostrar superheroe menos pesado ",
        "8 Salir"
    ]
    for opcion in lista_menu:
        print(opcion)
    return lista_menu

mostrar_menu_opciones()

def ingreso_opciones():
    
    for opcion in mostrar_menu_opciones():
        opcion = input("Ingrese una opcion: ")
        print(opcion)
    
    return opcion

ingreso_opciones()

def opciones():
    opcion = mostrar_menu_opciones() 
    continuar = True
    while continuar:
        opcion = ingreso_opciones(opcion)
        if opcion == 1:
            imprimir_nombre_superheroes()
            print("Opcion uno elegida")
        elif opcion == 2:
            imprimir_nombre_altura_superheroes()
            print("Opcion dos elegida")
        elif opcion == 3:
            imprimir_superheroe_mas_alto()
            print("Opcion tres elegida")
        elif opcion == 4:
            imprimir_superheroe_mas_bajo()
            print("Opcion cuatro elegida")
        elif opcion == 5:
            imprimir_promedio_alturas_superheroes()
            print("Opcion cinco elegida ")
        elif opcion == 6:
            imprimir_superheroe_mas_pesado()
            print("Opcion seis elegidas ")
        elif opcion == 7:
            imprimir_superheroe_menos_pesado()
            print("Opcion siete ")
        elif opcion == 8:
            print("Opcion salir ")
            continuar = False
        else:
            print("Error Ingrese nuevamente una opcion: ")
    return opcion

opciones()

# def listar_opciones(opciones):

#     opciones = {
#     "1" : imprimir_nombre_superheroes,
#     "2" : imprimir_nombre_altura_superheroes,
#     "3" : imprimir_superheroe_mas_alto,
#     "4" : imprimir_superheroe_mas_bajo,
#     "5" : imprimir_promedio_alturas_superheroes,
#     "6" : imprimir_superheroe_mas_pesado,
#     "7" : imprimir_superheroe_menos_pesado
#     }
    
#     return opciones

# listar_opciones()

