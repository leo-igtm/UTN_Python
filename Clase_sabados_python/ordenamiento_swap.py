lista = [ 2, 5, 3, 1, 6, 4 ]

print("Lista desordenada")
print(lista)

bandera_swap = True
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if(lista[i] > lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print("Lista ordenada")
print(lista)


while bandera_swap == True:
    bandera_swap = False
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            bandera_swap = True

print("Lista ordenada")
print(lista)


lista = [ {"nombre":"Tito", "edad":32, "nota":6},
          {"nombre":"Job", "edad":37, "nota":7},
          {"nombre":"Ana", "edad":25, "nota":9},
          {"nombre":"Juan", "edad":28, "nota":8},
          {"nombre":"Jose", "edad":23, "nota":4}
        ]

bandera_swap = True

print("Lista desordenada: ")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])



