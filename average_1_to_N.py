nbr = input("Enter a number > 1 : ")

def average_1_to_N(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i       
    return sum / n

print("The average is : ", average_1_to_N(nbr))