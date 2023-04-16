'''
Leonardo Figueroa Div f
Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido

'''

lista_de_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
numeros_de_lista = range(len(lista_de_numeros))#cuenta la cantidad de numeros que posee en una lista en un rango


print("esta es la cantidad de numeros: ",numeros_de_lista)

for i in range(len(lista_de_numeros)):
    for j in range(len(lista_de_numeros)):
        if j > i and lista_de_numeros[i] == lista_de_numeros[j]:
            print("El numero repetido :" ,lista_de_numeros[i])
            break