def polyarea(x, y):
    
    a = x[len(x)-1]*y[0] - y[len(x)-1]*x[0]  
    for i in range(0, len(x) - 1, 1):
        a += x[i] * y[i + 1] - y[i] * x[i + 1]
    return 0.5 * abs(a)


x = [0, 2, 2, 1, 0]
y = [0, 0, 2, 3, 2]

print("Pentagon : ", polyarea(x, y))

x = [0, 2, 2, 0]
y = [0, 0, 2, 2]

print('Area quadrilateral : ', polyarea(x, y))

x = [0, 2, 0]
y = [0, 0, 2]

print('Area triangle : ', polyarea(x, y))