



import matplotlib.pyplot as plt
import numpy as np

def f(x,y):   #diffrential equation function
    F= (y/x) - ((y/x)**2)
    return F



def Eulr_diff(y,xi,xf,h): #rk4   y is a np array/list containing initial value
                    #xi initial x , xf final x, h step size
    
    #h = (xf-xi)/n
    x = xi
    n= int(np.floor((xf-xi)/h))#number of mesh points
    
    for i in range(0,n-1):        
        x = x + h
        y.append(y[i] + h*f(x,y[i]))
        #print(y)
        
    xp = np.linspace(xi,xf,n)
    yp = xp/(1+ np.log(xp))

    plt.scatter(xp,y,c='k',label='Euler method')    #marker='o'
    plt.plot(xp,yp,'b',label='Exact solution')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.legend()
    plt.grid()
    plt.show()
    
    err=abs(yp-y)
    rel=abs(((yp-y)/yp))
    plt.plot(xp,err)
    plt.title('Absolute error')
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('abs error(t)')
    plt.show()
    plt.plot(xp,rel)
    plt.title('Relative error')
    plt.xlabel('t')
    plt.ylabel('rel error(t)')
    plt.grid()
    plt.show()
    
    print('Absolute Error:',err)
    print('Relative Error:',rel)
    
    
    
    
    return()


y = [1]
xi=1
xf=2
h=0.1

Eulr_diff(y,xi,xf,h)







