from math import pi
r = 10.6
a = 1.3
area_circle = pi*r**2
b = 0
while b * a < area_circle:
    b += 1

b -= 1

print("B = ", b)
