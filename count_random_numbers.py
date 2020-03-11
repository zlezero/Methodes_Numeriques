from random import randint

N = input("Enter N : ")

compteur = 0

for i in range(N):
    randNumber = randint(1, 6)
    print(randNumber)
    if randNumber == 6:
        compteur += 1

print "Compteur =", compteur, "Compteur/N =", float(compteur) / float(N)