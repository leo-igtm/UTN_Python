'''
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
'''
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
contador = 0
flag = False
for edad in edades:
    if flag == False or edad > edad_mas_joven:
        edad_mas_joven = edad
        indice = contador
        flag = True
    contador -= 1
print("La persona {0} de edad {1} es la mas joven ".format(nombre[indice+1],edades[indice+1]))

