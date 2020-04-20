
# Substituting t= tan(theta) the equation converts into
# dx/d(theta) = 1/((x^2)*(cos(theta))^2 + (sin(theta))^2)
#this reduces the t domain from [0,infinity) to [0,pi/2) 
#Here y serves as x and x serves as theta





import matplotlib.pyplot as plt
import numpy as np

def f(x,y):    #function to be integrated
    F= 1/((np.sin(x))**2  + (y**2)*(np.cos(x))**2) 
    return F

def rk4(y,xi,xf,h): #rk4   y is a np array/list containing initial value
                    #xi initial x , xf final x, h step size
    
    #h = (xf-xi)/n
    x = xi
    n= int(np.floor((xf-xi)/h))#number of mesh points
    
    for i in range(0,n-1):
    
        k1 = h*f(x,y[i])
        k2 = h*f(x+h/2,y[i]+k1/2)
        k3 = h*f(x+h/2,y[i]+k2/2)
        k4 = h*f(x+h,y[i]+k3)
        x=x+h
        y.append(y[i] + ((k1+2*k2+ 2*k3+k4)/6))

    xp = np.linspace(xi,xf,n)
    xp = np.tan(xp)
    
    print('x(3.5*1e-6) =',y[-1])
    plt.semilogx(xp,y,'g')
    plt.scatter(3.5*1e6,y[-1],c = 'r',marker='o')
    plt.title('x(t) vs t')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.grid()
    plt.show()
    return


y = [1]
xi=0
xf=np.pi/2
h=0.0001

rk4(y,xi,xf,h)






