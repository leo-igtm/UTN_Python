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

    if not nombre_heroe:
        return 'N/A'
    nombre_formateado = nombre_heroe.upper()
    nombre_formateado.replace('THE','')
    nombre_formateado.replace('-','')
    nombre_formateado.strip()
    for lista_heroe in nombre_formateado.split():
        if lista_heroe :
            inicial_formateado = '.'.join(lista_heroe[0]) + '.'
            print(f"{inicial_formateado}")
        else:
            return 'N/A'
    return 

extraer_iniciales("Spider-Man")


# cadena = "Leonardo Figueroa"
# cadena = cadena.strip()

# if "Nardo" == cadena:
#     inicial = cadena.replace('Hart','')
#     print(inicial)
# #print(cadena.split(","))