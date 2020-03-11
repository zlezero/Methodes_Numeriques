from numpy import *

N = input("Give the number of check points N : ")
epsilon = input("Give the error tolerance : ")

x = linspace(-4, 4, N)

def f(x):
    return x

def g(x):
    return x*x
    
for i in range(N):
    if abs(f(x[i]) - g(x[i])) < epsilon:
        print x[i]

