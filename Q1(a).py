

# Eular's Method

import matplotlib.pyplot as plt
import numpy as np

def f(x,y):   #diffrential equation function
    F= -9*y
    return F

def Eulr_diff(y,xi,xf,h): #rk4   y is a np array/list containing initial value
                    #xi initial x , xf final x, h step size
    
    #h = (xf-xi)/n
    x = xi
    n= int(np.floor((xf-xi)/h)) #number of mesh points
    
    for i in range(0,n-1):       
        x = x + h  
        
        y.append((y[i]/(1+9*h)))
        #print(y)
        
    xp = np.linspace(xi,xf,n)
    yp = np.exp( -9*xp + 1)   #Correct analytical function

    plt.plot(xp,yp,'k',label='Exate solution')   
    plt.scatter(xp,y,c='b',label='Backward intgration')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()
    return()



y = [np.exp(1)]
xi=0
xf=1
h=0.1


Eulr_diff(y,xi,xf,h)







