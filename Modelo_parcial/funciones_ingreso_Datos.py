import re

def validar_opcion(texto:str):

    while True:
        opcion = input(texto)
        if re.match(r'^(asc|desc)$',opcion,re.IGNORECASE):
            return opcion.upper()
        else:
            print("Porfavor ingrese una opcion asc|desc") 
    
print(validar_opcion("Ingrese orden asc|desc para ordenar la lista: "))

def esNumero(texto:str):
    while True:
        valor = input(texto)
        if re.match('^\d+$',valor):
            return int(valor)
        else:
            print("Porfavor ingrese una valor valido entero: ") 

print(esNumero("Ingrese un valor positivo: "))