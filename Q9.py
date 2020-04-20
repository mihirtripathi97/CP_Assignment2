# This code has been created with help from Bubai Rahman
import numpy as np
import matplotlib.pyplot as plt



def f(t,y):       # define y'
    return (y**2+y)/t

#exact solution
def y_true(t):
    return 2*t/(1-2*t)
    
ti =1
tf =3            #range of t value
ini_val = -2     #initial condition

h_min = 0.01     
N_max = int((tf-ti)/h_min) #maximum number of steps

y = np.zeros(N_max+1)    #array to store the solution
t = np.zeros(N_max+1)    # mesh points

t[0] = ti
y[0] = ini_val

Tol = 1e-5          #tolarence
i = 0
j = 0

h = h_min         #initial stepsize

while( t[j] < tf ):

#step size = 2h

    k1 = 2*h*f(t[j], y[j])
    k2 = 2*h*f(t[j]+h, y[j] + k1/2)
    k3 = 2*h*f(t[j]+h, y[j] + k2/2)
    k4 = 2*h*f(t[j]+2*h, y[j] + k3)
    Y = y[j] + ((k1+2*k2+2*k3+k4)/6)
        
#step size = h

    for i in range(2):
        k1 = h*f(t[i+j],y[i+j])
        k2 = h*f(t[i+j]+h/2,y[i+j]+k1/2)
        k3 = h*f(t[j+i]+h/2,y[i+j]+k2/2)
        k4 = h*f(t[j+i]+ h,y[i+j]+k3)
        y[i+j+1] = y[i+j] + (k1+2*k2+2*k3+k4)/6
        t[i+j+1] = t[i+j] + h

    d_t = abs( y[j+2]- Y)    #Differene between the two solutions with step size h and 2h
    
    for i in range(2):
        y[i+j+1] = y[i+j+1] + d_t/15    #adding correction term to the solution
    
    k = h*(Tol/d_t)**0.2
    
    if (t[j+2]+2*h>tf):
        h = (tf-t[j+2])/2
    
    elif (k<h):
        h = h_min
    else:
        h = k

    j = j + 2

y.resize((j+1))   #reducing size of the array
t.resize((j+1))

tp = np.linspace(1,3,200)

plt.scatter(t,y,c='r',label = 'Numerical solution')
plt.plot(tp,y_true(tp),'g',label = 'Exact solution')

plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.show()







