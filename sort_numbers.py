from random import *

listeNombres = list()

for i in range(10):
    listeNombres.append(uniform(0, 10))

def tri(liste):
    for i in range (len(liste)-2):
        min = i
        for j in range (i + 1, len(liste) - 1):
            if liste[j] < liste[min]:
                min = j
        if min != i:
            liste[i] = liste[min]
    return liste
            
print(tri(listeNombres))