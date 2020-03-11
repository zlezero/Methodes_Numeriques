import string

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']
decks = []

for suit in suits:
    for rank in ranks:
        decks.append(suit + rank)

print decks


letters = string.ascii_uppercase
nbr = range(10)
combinaisons = []

for lettre1 in letters:
    for lettre2 in letters:
        for nbr1 in nbr:
            for nbr2 in nbr:
                for nbr3 in nbr:
                    combinaisons.append('%s%s%s%s%s' % (lettre1, lettre2, nbr1, nbr2, nbr3))

print combinaisons

dice = range(1, 7)
compteur = 0

for de1 in dice:
    for de2 in dice:
        if de1 + de2 == 7:
            compteur += 1

print "Nbr of combinations equal 7 : ", compteur