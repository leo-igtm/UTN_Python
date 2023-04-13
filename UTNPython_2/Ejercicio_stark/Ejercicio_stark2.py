#1.1
# Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)
# ● En el caso que el nombre del personaje contenga el artículo ‘the’ se
# deberá omitir de las iniciales
# ● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
# que lo tenga se deberá reemplazar por un espacio en blanco
# 1.2
from data_stark import lista_personajes


def extraer_iniciales(nombre_heroe:str):

    for iniciales_personaje in lista_personajes:
        iniciales = iniciales_personaje["nombre"]
        if nombre_heroe == ' ':
            iniciales = '.'.join(iniciales) + '.'
    return iniciales_personaje

extraer_iniciales("Howard")


# cadena = "Leonardo Figueroa"
# cadena = cadena.strip()

# if "Nardo" == cadena:
#     inicial = cadena.replace('Hart','')
#     print(inicial)
# #print(cadena.split(","))