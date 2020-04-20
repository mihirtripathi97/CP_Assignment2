



import matplotlib.pyplot as plt
import numpy as np

def f(x,p,y):    #diffrential equation function
    F = ((x**3)*np.log(x)-2*y+2*x*p)/(x**2)
    return F
def fp(x,y):
    return(y)

def Eulr_diff(y,y_,xi,xf,h):       #   y is a np array/list containing initial value
                                   #xi initial x , xf final x, h step size
    
    #h = (xf-xi)/n
    x = xi
    n= int(np.floor((xf-xi)/h))#number of mesh points
    
    for i in range(0,n-1):
        
        
        
        y.append(y[i] + h*y_[i])
        y_.append(y_[i] + h*f(x,y_[i],y[i]))
        x = x + h
        
        
        
    xp = np.linspace(xi,xf,n)
    
    
    yp = (7*xp/4) + (((np.log(xp))/2) - 3/4)*(xp**3)

    plt.plot(xp,y,c='k',label='Euler Method')    #marker='o'
    plt.plot(xp,yp,'b',label='Exact Solution')
    plt.legend()
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.show()
    return()



y = [1]
y_ = [0]
xi=1
xf=2
h=0.001

Eulr_diff(y,y_,xi,xf,h)
        
        







