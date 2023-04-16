animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

temporadas = [1,5,1,2,3,6,4,8,4,6,4,6,3,2,1,5,4,2,6]
temporadas[:] = []
for anime in animes_90s:    
    nombre = anime["nombre"]
    if "temporadas" in anime and anime["temporadas"] > 1:
        temporadas.append(anime["nombre"])
print(temporadas)
         

#realiza una cantidad de vueltas de forma determinada
range(10)  

#Recorrer la lista contanto la cantidad de elementos que tiene la lista
range(len(animes_90s))

