from data import lista_bzrp

minimo = None
titulo_menor_reproducciones = None

# for video in lista_bzrp:
#     if minimo == None or video["views"] < minimo:
#         minimo = video["views"]
#         titulo_menor_reproducciones = video["title"]

# print("Minimo vistas: ", titulo_menor_reproducciones, minimo)

def imprimir_vistas_minima():#creamos la funcion
    'Muestra la cantidad de vistas minimas'  
    minimo = None
    titulo_menor_reproducciones = 0

    for video in lista_bzrp:#lista | diccionario
        if minimo == None or video["views"] < minimo:
            minimo = video["views"]
            titulo_menor_reproducciones = video["title"]
            
    print("Minima cantidad de vistas: ", titulo_menor_reproducciones, minimo)
    return

imprimir_vistas_minima()#se llama la funcion

def imprimir_vistas_maximas():#creamos la funcion
    'Muestra la cantidad de vistas minimas'  
    mayor_vistas_reproducciones = None
    titulo_mayor_reproducciones = None

    for video in lista_bzrp:#lista | diccionario
        if mayor_vistas_reproducciones == None or video["views"] > mayor_vistas_reproducciones:
            mayor_vistas_reproducciones = video["views"]
            titulo_mayor_reproducciones = video["title"]
            
    print("Maxima cantidad de vistas: ", titulo_mayor_reproducciones, minimo)
    return
imprimir_vistas_maximas()

def menu_opciones():
    
    print("1 mostrar minimo ")
    print("2 mostrar maximo ") 
    print ("3 mostrar promedio ")
    print("4 salir ") 
    opcion=input("Ingrese una opcion: ")
    opciones = int(opcion)
    return opciones

    continuar = True
    while continuar:
        opciones = menu_opciones()
        if opciones == 1:
            print("Opcion uno elegida")
        elif opciones == 2:
            print("Opcion dos elegida")
        elif opciones == 3:
            print("Opcion dos elegida")
        if opciones == 4:
            print("Opcion salir ")
        continuar = False
    