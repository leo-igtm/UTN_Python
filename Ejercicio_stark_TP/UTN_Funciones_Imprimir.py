from data_stark import lista_personajes

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