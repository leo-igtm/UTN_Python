# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos

ingreso_estacion = input("Ingrese una estacion de año: Invierno/Verano/Otoño/Primavera ")
ingreso_localidad = input("Ingrese una estacion de año:  Bariloche/Cataratas/Mar del Plata/Córdoba ")
ingreso_precio = input("Ingrese una estacion de año:  Bariloche/Cataratas/Mar del Plata/Córdoba ")
precio = int(ingreso_precio)
localidad = str(ingreso_localidad)
estacion = str(ingreso_estacion)

descuento = 0.1
print(descuento)
aumento = 0.2
precio_final = 0
while(estacion != "Invierno" and estacion != "Verano" and estacion != "Otoño" and estacion != "Primavera"):
    print("Localidad" , estacion)

while(localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mar del Plata" and localidad != "Córdoba"):
    print("Localidad",localidad)

while(precio <0 and precio >15000):
    print(precio ,"$")

match estacion:
    case "Invierno":
        if(localidad =="Bariloche"):
            aumento *= 0.2
        if(localidad == "Cataratas" and localidad == "Cordoba"):
            descuento *= 0.1
        if(localidad == "Mar del Plata"):
            descuento = 0.2
    case "Otoño":
        if(localidad =="Bariloche"):
            aumento = 0.2
        if(localidad == "Cataratas" and localidad == "Cordoba"):
            descuento = 0.1
        if(localidad == "Mar del Plata"):
            descuento = 0.2 
    case "Primavera":
        if(localidad =="Bariloche"):
            aumento = 0.2
        if(localidad == "Cataratas" and localidad == "Cordoba"):
            descuento = 0.1
        if(localidad == "Mar del Plata"):
            descuento = 0.2

    case "Verano":
        if(localidad =="Bariloche"):
            aumento = 0.2
        if(localidad == "Cataratas" and localidad == "Cordoba"):
            descuento = 0.1
        if(localidad == "Mar del Plata"):
            descuento = 0.2
