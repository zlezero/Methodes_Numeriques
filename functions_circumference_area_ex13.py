from math import pi

r = input("Enter the circle radius : ")

def calculate_circumference(r):
    return pi * r * 2

def calculate_area(r):
    return pi * r**2

print('The circumference is : %g' % calculate_circumference(r))
print('The area is : %g' % calculate_area(r))