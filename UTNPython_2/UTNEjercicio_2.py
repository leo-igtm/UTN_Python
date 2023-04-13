#Ejercicio 2:
#Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
#adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("ingrese edad: "))
print(type(edad))

respuesta = 's'
while(respuesta == 's'):
    respuesta = input("Desea continuar? s/n:")
    if(edad >= 18 ):
        print("es mayor de edad")
    elif(edad > 13 and edad < 17):
        print("es adolescente")
    else:
        print("es niño")
pass
