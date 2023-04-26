# Escribir un programa que le pida al usuario que ingrese su edad,
# y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, o
# "Eres menor de edad" si la edad es menor a 18.

edad_ingresada = input("Ingresar edad: ")
edad = int(edad_ingresada)

respuesta = 's'
while(respuesta == 's'):
    respuesta=input("Desea continuar? s/n:")
    if(edad < 0 or edad >= 18):
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
pass