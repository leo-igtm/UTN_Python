# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número ingresado es par" si el número es divisible por 2, o 
# "El número ingresado es impar" si el número no es divisible por 2.

ingreso_numero = input("Ingrese un numero: ")
numero_entero = float(ingreso_numero)


if(numero_entero % 2 == 0):#Condicion que indica que si el numero ingresado es par o impar 
    print("Es par")
else:
    print("Es impar")