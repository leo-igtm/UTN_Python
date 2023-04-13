#Leonardo Figueroa div F Dni:42588408
#Ejercicio 3:
#Ingresar 5 números enteros, distintos de cero.
#Informar:
#a. Cantidad de pares e impares.
#b. El menor número ingresado.
#c. De los pares el mayor número ingresado.
#d. Suma de los positivos.
#e. Producto de los negativos.

lista_numeros= list(range(10))

menor_numero = None
mayor_numero_par = None
cantidad_pares = 0
cantidad_impares = 0
producto_negativos = 1
suma = 0


for numero in lista_numeros:

    if(numero % 2 == 0):
        cantidad_pares += 1
    
    if(mayor_numero_par == None or numero > mayor_numero_par):
        mayor_numero_par = numero
    if(menor_numero == None or numero < menor_numero):
        menor_numero = numero
    else:
        cantidad_impares += 1
    if(numero > 0):
        suma = cantidad_pares + mayor_numero_par
    elif(menor_numero < 0):
        producto_negativos *= numero
        

print("Cantidades pares: ", cantidad_pares)
print("Mayor numero par ingresado: ", mayor_numero_par)
print("Menor numero ingresado: ", menor_numero)
print("Cantidades impares: " ,cantidad_impares)
print("Suma de los positivos" ,suma)
print("Productos de los negativos: ",producto_negativos)
print("Menor numero ", producto_negativos)        
pass


