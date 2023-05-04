
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

1.3. Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
como parámetro:

● lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes
seguido de las iniciales encerradas entre paréntesis ()
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
…
La función no retorna nada

2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como
parámetros:
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero
● genero_heroe: un string que representa el género del héroe ( puede
tomar los valores ‘M’, ‘F’ o ‘NB’)
La función deberá generar un string con el siguiente formato:
GENERO-000…000ID
Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
último el identificador recibido. Todos los códigos generados deben tener
como máximo 10 caracteres (contando todos los caracteres, inclusive el
guión). Se deberá completar con ceros para que todos queden del mismo
largo
Algunos ejemplos:
F-00000001
M-00000002
NB-0000010
La función deberá validar:
● El identificador del héroe sea numérico.
● El género no se encuentre vacío y este dentro de los valores esperados
(‘M’, ‘F’ o ‘NB’)
En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
correctamente retornar el código generado
'''
from data_stark import lista_personajes

lista_heroes =  [{'nombre': 'Iron Man', 'altura': 1.74, 'peso': 123, 'genero': 'M'}, {'nombre': 'Howard the Duck', 'altura': 1.74, 'peso': 123, 'genero': 'NB'}, {'nombre': 'The Enchantress', 'altura': 1.74, 'peso': 123, 'genero': 'F'}]

def extraer_iniciales(nombre_heroe:str) -> str:
    '''Recibe un string por parametro y  imprime solo las iniciales cada una seguida por un punto'''
    if not nombre_heroe:
        return 'N/A'
    nombre_formateado = nombre_heroe.upper()
    nombre_formateado.replace('THE','')
    nombre_formateado.replace('-','')
    nombre_formateado.strip()
    iniciales = ''
    for palabra in nombre_formateado.split():
        if palabra:
            iniciales += palabra[0] + '.'
            print(iniciales)
    if iniciales:
        return iniciales
    
    return 'N/A'

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
    
    if type(lista_heroes) != list or len(lista_heroes) < 1:
        return False
    flag = 0
    for heroe in lista_heroes:
        if definir_iniciales_nombre(heroe) == False:
            flag = 1
            print("Formato incorrecto")
            break
        else:
            definir_iniciales_nombre(heroe)
    if flag == 1:
        return False
    else:
        return True

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    
    if type(lista_heroes) != list or len(lista_heroes) < 1:
        return False
    agregar_iniciales_nombre(lista_heroes)
    for heroe in lista_heroes:
        if heroe["iniciales"] is None:
            heroe["iniciales"] = ""
        print('* '.join(heroe["nombre"]) + '( '.join(heroe["iniciales"]) + ') ')


print(agregar_iniciales_nombre(lista_heroes))
stark_imprimir_nombres_con_iniciales(lista_heroes)


