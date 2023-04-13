#Leonardo Figueroa Div F DNI:42588408
# Ejercicio 4:
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.'

ingreso_edad = input("ingrese edad: ")
estado = input("Ingrese estado civil: ")
edad = int(ingreso_edad)
estado_civil = str(estado)

if(edad < 18 and estado_civil != "Soltero"):
    print("Es muy pequeño para NO ser soltero")
else:
    print("Es menor de 18")

