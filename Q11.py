

import matplotlib.pyplot as plt
import numpy as np

def U1(t,u1,u2,u3):    #function to be diffrentiated
    F = u1 + 2*u2 - 2*u3 + np.exp(-t)
    return F

def U2(t,u1,u2,u3):    #function to be diffrentiated
    F = u2 + u3 - 2*np.exp(-t)
    return F

def U3(t,u1,u2,u3):    #function to be diffrentiated
    F = u1 + 2*u2  + np.exp(-t)
    return F



def rk4(u1,u2,u3,xi,xf,h): #rk4   y is a np array/list containing initial value
                    #xi initial x , xf final x, h step size
  
    #h = (xf-xi)/n
    x = xi
    n= int(np.floor((xf-xi)/h))#number of mesh points

    for i in range(0,n-1):
    
        k11 = h*U1(x,u1[i],u2[i],u3[i])
        k21 = h*U2(x,u1[i],u2[i],u3[i])
        k31 = h*U3(x,u1[i],u2[i],u3[i])
         
        k12 = h*U1(x+h/2, u1[i]+k11/2, u2[i]+k21/2, u3[i]+k31/2)
        k22 = h*U2(x+h/2, u1[i]+k11/2, u2[i]+k21/2, u3[i]+k31/2)
        k32 = h*U3(x+h/2, u1[i]+k11/2, u2[i]+k21/2, u3[i]+k31/2)
        
        k13 = h*U1(x+h/2, u1[i]+k12/2, u2[i]+k22/2, u3[i]+k32/2)
        k23 = h*U2(x+h/2, u1[i]+k12/2, u2[i]+k22/2, u3[i]+k32/2)
        k33 = h*U3(x+h/2, u1[i]+k12/2, u2[i]+k22/2, u3[i]+k32/2)
        
        
        
        k14 = h*U1(x+h, u1[i]+k13, u2[i]+k23, u3[i]+k33)
        k24 = h*U2(x+h, u1[i]+k13, u2[i]+k23, u3[i]+k33)
        k34 = h*U3(x+h, u1[i]+k13, u2[i]+k23,u3[i]+k33)  

        u1.append(u1[i] + ((k11+ 2*k12 + 2*k13 + k14)/6))                     
        u2.append(u2[i] + ((k21 + 2*k22 + 2*k23 + k24)/6))      
        u3.append(u3[i] + ((k31 + 2*k32 + 2*k33 + k34)/6))
        
        
        x=x+h

    xp = np.linspace(xi,xf,n)
    
    print(xp[-1])
    plt.plot(xp,u1,'r',marker='o')
    plt.plot(xp,u2,'g',marker='o')
    plt.plot(xp,u3,'b',marker='o')
    plt.show()
    return()


u1 = [3]
u2 = [-1]
u3 = [1]

ti=0
tf = 1
h=0.05


rk4(u1,u2,u3,ti,tf,h)







