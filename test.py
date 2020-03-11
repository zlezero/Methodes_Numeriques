from math import exp

def trapez(f, a, b, n):
    h = (b - a) / n
    S = 0.0
    xg = a
    xd = a + h
    for k in range(n):
        s = h * (f(xg) + f(xd)) / 2
        S += s
        xg += h
        xd += h
    return S

def f(t):
    return 3*t**2*exp(t**3)

a = 0.0
b = 1.0
n = 1000

S = trapez(f, a, b, n)
print(S)