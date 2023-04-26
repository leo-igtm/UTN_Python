
'''
1.1
Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
● nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con
las iniciales del nombre del personaje seguidos por un punto (.)
● En el caso que el nombre del personaje contenga el artículo ‘the’ se
deberá omitir de las iniciales
● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
que lo tenga se deberá reemplazar por un espacio en blanco

# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como
parámetro:
● heroe: un diccionario con los datos del personaje
La función deberá agregar una nueva clave al diccionario recibido como
parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
llamar a la función ‘extraer_iniciales’
La función deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave ‘nombre’
En caso de encontrar algún error retornar False, caso contrario retornar True

1.3. Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
parámetro:
● lista_heroes: lista de personajes
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada héroe a la función
definir_iniciales_nombre.
En caso que la función definir_iniciales_nombre() retorne False entonces se
deberá detener la iteración e informar por pantalla el siguiente mensaje:
‘El origen de datos no contiene el formato correcto’
La función deberá devolver True en caso de haber finalizado con éxito o False
en caso de que haya ocurrido un error
'''
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str):
    '''Recibe un string por parametro y  imprime solo las iniciales cada una seguida por un punto'''
    if not nombre_heroe:
        return 'N/A'
    nombre_formateado = nombre_heroe.upper()
    nombre_formateado.replace('THE','')
    nombre_formateado.replace('-','')
    nombre_formateado.strip()
    for lista_heroe in nombre_formateado.split():
        if lista_heroe != '':
            inicial_formateado = '.'.join(lista_heroe[0]) + '.'
            print(inicial_formateado)
        else:
            return 'N/A'
    return 

extraer_iniciales("Leonardo Figueroa")

def definir_iniciales_nombre(heroe:dict):
    heroe['iniciales'] = extraer_iniciales(heroe['nombre']) 
    if type(heroe) != dict or 'nombre' in heroe:
        print(heroe['iniciales'])
    else:    
        return False
    return 

definir_iniciales_nombre({'nombre':'Superman','inicial':'S'})

def agregar_iniciales_nombre(lista_heroes:list):
    return