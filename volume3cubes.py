from numpy import linspace
from matplotlib.pyplot import *

L = linspace(1,3,3)
V = L**3
print "Volumes :", V
plot(L, V)
xlabel('Length of side')
ylabel('Volume')
show()