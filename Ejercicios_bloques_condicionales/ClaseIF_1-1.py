# Escribir un programa que le pida al usuario que ingrese un número entero positivo,
# y luego imprima "El número ingresado es positivo" si el número es mayor que cero, o 
# "El número ingresado es cero o negativo" si el número es menor o igual a cero.

ingreso_numero = input("Ingrese un numero: ")
numero_entero = int(ingreso_numero)

respuesta = 's'
while(respuesta == 's'):
    respuesta=input("Desea continuar? s/n:")
    if(numero_entero > 0):
        print("El numero es positivo")
    elif(numero_entero <= 0):
        print("El número ingresado es cero o negativo")
