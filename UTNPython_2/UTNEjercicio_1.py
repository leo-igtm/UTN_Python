#Ejercicio 1:
#Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
#sueldo para esa persona.

nombre = input("ingrese nombre: ")
sueldo = input("Ingrese sueldo: ")
sueldo = int(sueldo)
incremento_sueldo =  0.1

print(sueldo)
print(type(sueldo))

sueldoincrementado = sueldo * (incremento_sueldo / 100) #Incremento de sueldo al 10% 

print("El nombre es: \n", nombre, "\n su sueldo incrementado es:  \n" ,sueldo)
