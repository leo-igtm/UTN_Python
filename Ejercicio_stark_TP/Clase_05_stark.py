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

# heroe_masculino = lista_personajes[0]["genero"]
# heroe_femenino = lista_personajes[0]["genero"]
# heroe_mas_Alto = lista_personajes[0]["altura"]
# heroe_mas_bajo = lista_personajes[0]["altura"]

# maximo_altura_superheroe = float(heroe_mas_Alto)
# minima_altura_superheroe = float(heroe_mas_bajo)

# def mostrar_heroe_masculino(lista_personajes,ingresar_genero=str):
#     for lista in lista_personajes:
#         nombre_heroe_masculino = lista["nombre"]
#         genero_heroe = lista["genero"]
#         if genero_heroe == ingresar_genero:
#             print("Personajes: " ,nombre_heroe_masculino ,"| Genero: ", genero_heroe)
#             print("<------------------------------------------------------------------>")
#     return nombre_heroe_masculino,genero_heroe

# mostrar_heroe_masculino(lista_personajes,"M")

# def imprimir_superheroe_alto(lista_personajes,ingresar_genero=str):
    
#     for lista in range(len(lista_personajes)):
#         altura_max_heroe = float(lista_personajes[lista]["altura"])

#         if lista == 0 or altura_max_heroe > heroe_mas_Alto :
#             heroe_mas_Alto = altura_max_heroe
#             if heroe_mas_Alto == ingresar_genero:
#                 ingresar_genero = heroe_mas_Alto
#             print(f"Personajes: {heroe_mas_Alto:.2f}","| Genero: ",ingresar_genero)
#             print("<------------------------------------------------------------------>")

#     return heroe_mas_Alto,ingresar_genero

# imprimir_superheroe_alto(lista_personajes,"M")

# def imprimir_superheroe_alto(lista_personajes,ingresar_genero=str):
    
#     for lista in range(len(lista_personajes)):
#         altura_min_heroe = float(lista_personajes[lista]["altura"])

#         if lista == 0 or altura_min_heroe < heroe_mas_bajo :
#             heroe_mas_bajo = altura_min_heroe
#             if heroe_mas_bajo == ingresar_genero:
#                 ingresar_genero = heroe_mas_bajo
#             print(f"Personajes: {heroe_mas_bajo:.2f}","| Genero: ",ingresar_genero)
#             print("<------------------------------------------------------------------>")

#     return heroe_mas_Alto,ingresar_genero

# imprimir_superheroe_alto(lista_personajes,"F")

def imprimir_promedio_superheroes(lista_personajes:list,ingresar_genero:str):
    suma_altura_superheroe = 0
    contador = 0
    for lista in lista_personajes:
        genero_superheroe = lista["genero"]
        altura_personajes = float(lista_personajes[0]["altura"])
        if genero_superheroe == ingresar_genero:
            suma_altura_superheroe += altura_personajes
            ingresar_genero = genero_superheroe
        contador +=1
        promedio_altura_superheroe =  suma_altura_superheroe / contador
    print("El promedio es: {0:.2f}".format(promedio_altura_superheroe), "| Genero: ", ingresar_genero)

    return promedio_altura_superheroe, ingresar_genero

imprimir_promedio_superheroes(lista_personajes,"M")

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def conteo_tipo_color_ojos(lista:list):
    conteo_color_ojos = {}
    for lista in lista_personajes:
        color_ojos = lista['color_ojos'].upper()
        if color_ojos not in conteo_color_ojos:
            conteo_color_ojos[color_ojos] = 0
        conteo_color_ojos[color_ojos] += 1 
    return conteo_color_ojos

conteo_tipo_color_ojos(lista_personajes)

# M. listar todos los superhéroes agrupados por color de ojos.

def listar_tipo_color_ojos(lista_heroes:list,clave:str):

    diccionario = {}
    conteo_color_ojos = conteo_tipo_color_ojos(lista_heroes)

    if not lista_heroes and clave not in lista_heroes[0]:
        return {}
    
    for heroes in lista_heroes:
        if clave in heroes and heroes[clave] != "":
            resultado_clave = heroes[clave]
        else:
            resultado_clave = 'No tiene'

        if resultado_clave in diccionario:
            diccionario[resultado_clave].append(heroes)
        else:
            diccionario[resultado_clave] = [heroes]


        for conteo_color_ojos in diccionario[resultado_clave]:
            print("Personaje Color de ojos: ",conteo_color_ojos["color_ojos"],"\n") 
            print("<------------------------------------------------------------------------>") 
    return diccionario

listar_tipo_color_ojos(lista_personajes,'color_ojos')

# # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

# def conteo_tipo_color_pelo(lista):
#     conteo_color_pelo = {}
#     for lista in lista_personajes:
#         color_pelo = lista['color_pelo'].upper()
#         if color_pelo not in conteo_color_pelo:
#             conteo_color_pelo[color_pelo] = 0
#         conteo_color_pelo[color_pelo] += 1 

#     for color_pelo,cantidad in conteo_color_pelo.items():        
#         print("Personaje Color de pelo: ",color_pelo,"\n", "Cantidad superheroe: ",cantidad) 
#         print("<------------------------------------------------------------------------>")

#     return conteo_color_pelo,cantidad

# conteo_tipo_color_pelo(lista_personajes)


# # L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
# def conteo_tipo_inteligencia(lista_personajes:list,ingresar_tipo:str):
#     conteo_tipo_inteligencia = {}
#     for heroe in lista_personajes:
#         if ingresar_tipo in heroe and heroe[ingresar_tipo].upper() != '':
#             inteligencia = heroe[ingresar_tipo]
#         else:
#             inteligencia = 'No tiene'

#         if inteligencia not in conteo_tipo_inteligencia:
#             conteo_tipo_inteligencia[inteligencia] = 0
#         conteo_tipo_inteligencia[inteligencia] += 1 

#     for inteligencia,cantidad in conteo_tipo_inteligencia.items():        
#         print("Personaje tipo de inteligencia: ",inteligencia,"\n", "Cantidad superheroe: ",cantidad) 
#         print("<------------------------------------------------------------------------>")
    
# imprimir_tipo_inteligencia(lista_personajes,'inteligencia')




