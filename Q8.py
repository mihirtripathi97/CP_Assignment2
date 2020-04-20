

import numpy as np

import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp


n = int((input("Which problem do you want to solve (from 1 to 4):")))

if(n==1):
    
    def f(x,y):    
            return np.vstack((y[1], -np.exp(-2*y[0])))
    def bc(ya, yb):    
            return np.array([ya[0], yb[0]-np.log(2)])
    
    x = np.linspace(1, 2, 5)
    y = np.zeros((2, x.size))
    res = solve_bvp(f, bc, x, y)
    x_plot = np.linspace(1, 2, 100)
    y_plot = res.sol(x_plot)[0]
    plt.plot(x_plot, y_plot, label='Numerical solution for 1')    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()    
    plt.show()   
    
elif(n==2):
        
    def f(x,y):    
            return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))
    def bc(ya, yb):    
            return np.array([ya[0]-1,yb[0]-np.exp(1)])
    
    x = np.arange(0, np.pi/2, np.pi/10)
    y = np.zeros((2, x.size))
    y[0]=2
    sol = solve_bvp(f, bc, x, y)
    plt.plot(sol.x,sol.y[0], label='Numerical solution for 2')    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()    
    plt.show()   
    
    
elif(n==3):
        
    def f(x,y):    
            return np.vstack((y[1],(-1/np.cos(x))*(2*y[1]**3+y[0]**2*y[1])))
    def bc(ya, yb):    
            return np.array([ya[0]-2**(-1/4),yb[0]-12**(1/4)/2])
    
    x = np.arange(np.pi/4,np.pi/3,np.pi/100)
    y = np.zeros((2,x.size))
    y[0] = (2**(-1/4))
    sol = solve_bvp(f, bc, x, y)
    plt.plot(sol.x,sol.y[0], label='Numerical solution for 2')    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()    
    plt.show()   
    
elif(n==4):
    def f(x,y):
        return np.vstack((y[1],0.5-y[1]**2-y[0]*np.sin(x)/2))
    def bc(ya,yb):
        return np.array([ya[0]-2,yb[0]-2])
    x=np.arange(0,np.pi,np.pi/10)
    y=np.zeros((2,x.size))
    sol=solve_bvp(f,bc,x,y)
    plt.plot(sol.x,sol.y[0],label="Numerical Solution")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

else:
    print("Wrong choice!")



