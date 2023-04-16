# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia
from data_stark import lista_personajes

heroe_masculino = lista_personajes[0]["genero"]
heroe_femenino = lista_personajes[0]["genero"]
heroe_mas_Alto = lista_personajes[0]["altura"]
heroe_mas_bajo = lista_personajes[0]["altura"]

maximo_altura_superheroe = float(heroe_mas_Alto)
minima_altura_superheroe = float(heroe_mas_bajo)

def listar_heroe_masculino(lista_personajes,ingresar_genero=str):
    for lista in lista_personajes:
        nombre_heroe_masculino = lista["nombre"]
        genero_heroe = lista["genero"]
        if genero_heroe == ingresar_genero:
            print("Personajes: " ,nombre_heroe_masculino ,"| Genero: ", genero_heroe)
            print("<------------------------------------------------------------------>")
    return nombre_heroe_masculino,genero_heroe

listar_heroe_masculino(lista_personajes,"F")

def listar_superheroe_alto(lista_personajes,ingresar_genero=str):
    
    for lista in range(len(lista_personajes)):
        altura_max_heroe = float(lista_personajes[lista]["altura"])

        if lista == 0 or altura_max_heroe > heroe_mas_Alto :
            heroe_mas_Alto = altura_max_heroe
            if heroe_mas_Alto == ingresar_genero:
                ingresar_genero = heroe_mas_Alto
            print(f"Personajes: {heroe_mas_Alto:.2f}","| Genero: ",ingresar_genero)
            print("<------------------------------------------------------------------>")

    return heroe_mas_Alto,ingresar_genero

listar_superheroe_alto(lista_personajes,"M")

def listar_superheroe_alto(lista_personajes,ingresar_genero=str):
    
    for lista in range(len(lista_personajes)):
        altura_min_heroe = float(lista_personajes[lista]["altura"])

        if lista == 0 or altura_min_heroe < heroe_mas_bajo :
            heroe_mas_bajo = altura_min_heroe
            if heroe_mas_bajo == ingresar_genero:
                ingresar_genero = heroe_mas_bajo
            print(f"Personajes: {heroe_mas_bajo:.2f}","| Genero: ",ingresar_genero)
            print("<------------------------------------------------------------------>")

    return heroe_mas_Alto,ingresar_genero

listar_superheroe_alto(lista_personajes,"F")

def listar_promedio_superheroes(lista_personajes,ingresar_genero):
    suma_altura_superheroe = 0
    for lista in lista_personajes:
        genero_superheroe = lista["genero"]
        altura_personajes = float(lista_personajes[0]["altura"])
        if genero_superheroe == ingresar_genero:
            suma_altura_superheroe += altura_personajes
            ingresar_genero = genero_superheroe
            promedio_altura_superheroe =  suma_altura_superheroe / len(lista)
    print("El promedio es: {0:.2f}".format(promedio_altura_superheroe), "| Genero: ", ingresar_genero)

    return promedio_altura_superheroe, ingresar_genero

listar_promedio_superheroes(lista_personajes,"F")

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def listar_superheroes_color_de_ojos(lista_personajes):
    color_ojos={}
    for lista in lista_personajes:
        color= lista.get('color_ojos','Unknown')
        color_ojos[color] = color_ojos.get(color,0) + 1
        print("Personajes color: ",color,"Cantidad: ",color_ojos[color])
    return
listar_superheroes_color_de_ojos(lista_personajes)




# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.




# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
