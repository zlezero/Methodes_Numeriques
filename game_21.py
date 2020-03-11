from random import randint

sum_J1 = 0
sum_J2 = 0

is_J1_turn = True
another_draw = False

def J1Lose():
    return sum_J1 > 21

def J1Win():
    if (J1Lose()):
        return False
    elif (J2Lose()):
        return True
    else:
        return sum_J1 > sum_J2

def J2Lose():
    return sum_J2 > 21

def J2Win():
    if (J2Lose()):
        return False
    elif (J1Lose()):
        return True
    else:
        return sum_J1 < sum_J2

def CurrentSum():
    return sum_J1 if (is_J1_turn) else sum_J2

while (sum_J1 <= 21 or sum_J2 <= 21):
    
    currentDraw = randint(0, 10)

    if is_J1_turn:
        print("\n=== Tour de J1 ===") if (not another_draw) else ""
        sum_J1 += currentDraw
    else:
        print("\n=== Tour de J2 ===") if (not another_draw) else ""
        sum_J2 += currentDraw

    print "Vous gagnez " + str(currentDraw) + ". Votre total est maintenant de :", CurrentSum()

    if (J1Lose() or J2Lose()):
        break

    inputAnotherDraw = ""

    while (inputAnotherDraw != 1 and inputAnotherDraw != 2):

        inputAnotherDraw = input("Voulez-vous retirer 1 = Oui / 2 = Non ? ")
        
        if (inputAnotherDraw == 2):
            if (not is_J1_turn):
                break
            else:
                is_J1_turn = not is_J1_turn
                another_draw = False
        elif (inputAnotherDraw == 1):
            another_draw = True

print("\nJ1 a gagné !") if (J1Win()) else ""
print("\nJ2 a gagné !") if (J2Win()) else ""
print("\nEgalité !") if (J1Win() and J2Win()) else ""


