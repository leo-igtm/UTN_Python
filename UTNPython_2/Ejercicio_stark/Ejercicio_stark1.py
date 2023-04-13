# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
from data_stark import lista_personajes

heroe_masculino = lista_personajes[0]["genero"]
heroe_femenino = lista_personajes[0]["genero"]
heroe_mas_Alto = lista_personajes[0]["altura"]
maximo_altura_superheroe = float(heroe_mas_Alto)

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