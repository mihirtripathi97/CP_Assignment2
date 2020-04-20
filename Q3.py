
import matplotlib.pyplot as plt
import numpy as np

def f2(y,y_,x):    #funcion to be integrated
   
    F = 2*y_ - y + x*np.exp(x) - x
    return F

def f1(y,y_,x):    #funcion o be integrated
    return y_





def rk_c_4(y,y_,xi,xf,h): #rk4   y is a np array/list conaining initial value
                    #xi initial x , xf final x, h step size
  
    #h = (xf-xi)/n
    x = xi
    n= int(np.floor((xf-xi)/h))#number of mesh poins

    for i in range(0,n-1):
        
        
        k11 = h*f1( y[i], y_[i], x)
        k21 = h*f2( y[i], y_[i], x)
        
        k12 = h*f1( y[i]+ 0.5*k11, y_[i] + 0.5*k21, x+0.5*h)
        k22 = h*f2( y[i]+ 0.5*k11, y_[i] + 0.5*k21, x+0.5*h)
        
        k13 = h*f1( y[i]+ 0.5*k12, y_[i] + 0.5*k22, x+0.5*h)
        k23 = h*f2( y[i]+ 0.5*k12, y_[i] + 0.5*k22, x+0.5*h)
        
        k14 = h*f1( y[i]+ k13, y_[i]+ k23, x+h)
        k24 = h*f2( y[i]+ k13, y_[i]+ k23, x+h)
  
        
        y.append(y[i] + ((k11 + 2*k12 + 2*k13 + k14)/6))        
        y_.append(y_[i] + ((k21 +2*k22 + 2*k23 + k24)/6))
        
        x=x+h

    xp = np.linspace(xi,xf,n)
     
   
    plt.plot(xp,y,'r',label='y(x)')    
    plt.plot(xp,y_,'g',label='y\'(x)')
    plt.grid(True)
    plt.show()
    
    return




xi=0
xf=1
y=[0]
y_=[0]
h=0.001


rk_c_4(y,y_,xi,xf,h)







