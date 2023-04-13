# Ejercicio 6:
# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor.

lista_de_numero = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

numero_mayor = 0

for indice in lista_de_numero:
    if(indice == 0 and indice > numero_mayor ):
        
        
        print()



def calculo_valor_con_iva(precio_unitario,iva):
    ''' Caculo de precio unitario mas iva de 21%'''
    resultado = precio_unitario * (1+(iva/100))
    return resultado