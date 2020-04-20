

from scipy.optimize import newton
from matplotlib import pyplot as plt
import numpy as np



def f(x,y):
    return(-20*(y-x)**2 + 2*x)

xi = 0
xf = 1
h = 0.1
n = 10
y0=1/3

x=np.linspace(xi,xf,n)
y=np.zeros(n)

y[0]=y0

for i in range(n-1):
    
    def F(z):
        return(z-y[i]-h*f(x[i+1],z))
    
    y[i+1]=newton(F,y[i])

plt.scatter(x,y,label='Backward integrationn',c='k')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show() 







