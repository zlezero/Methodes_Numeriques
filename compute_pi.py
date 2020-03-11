from numpy import sqrt, pi, zeros
import matplotlib.pyplot as plt

N = input("Enter N : ")

piMethodeA = 0
piMethodeB = 0

Leibniz_error = zeros(N)
Euler_error = zeros(N)

for i in range(1, N+1):
    piMethodeA += 1.0 / ((4*(i-1) + 1) * (4*(i-1) + 3))
    Leibniz_error[i-1] = pi - 8 * piMethodeA
    piMethodeB += 1.0 / (i ** 2)
    Euler_error[i-1] = pi - sqrt( 6 * piMethodeB)

piMethodeA *= 8

piMethodeB *= 6
piMethodeB = sqrt(piMethodeB)

print("Methode A : ", piMethodeA)
print("Methode B : ", piMethodeB)

erreurMethodeA = abs(pi - piMethodeA)
erreurMethodeB = abs(pi - piMethodeB)

print("Erreur methode A : ", erreurMethodeA)
print("Erreur methode B : ", erreurMethodeB)

plt.plot(range(N), Leibniz_error, 'b-', range(N), Euler_error, 'r-')
         
plt.xlabel('No of terms')
plt.ylabel('Error with Leibniz (blue) and Euler (red)')
plt.show()