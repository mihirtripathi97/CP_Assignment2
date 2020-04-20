


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def fun_1(t,y):
    F = t*np.exp(3*t) - 2*y
    return F

def fun_2(t,y):
    F = 1 - ((t - y)**2)
    return F

def fun_3(t,y):
    F = 1 + (y/t)
    return F

def fun_4(t,y):
    F = np.cos(2*t) + np.sin(3*t)
    return F

'''def ivp_solver(y,x_sp,n,f):
    
    xp = np.linspace(x_sp[0],x_sp[1],n)
    sol = solve_ivp(f, x_sp , y,t_eval=xp)
    #print(sol.t)
    #print(sol.y)
    plt.plot(sol.t,sol.y[0],'k')
    
    plt.plot(xp,yp,'b')
    plt.title("Ana fun 1")
    plt.show() 
    plt.title(f.__name__)
    plt.show()   
    return'''

#Question 1
y = [0]
x_sp=(0,1)

xp = np.linspace(x_sp[0],x_sp[1],25)
sol = solve_ivp(fun_1, x_sp , y, method='BDF',t_eval=xp)
plt.scatter(sol.t,sol.y[0],c='b',label='Using solve_ivp')

yp = (np.exp(3*xp))*(-(1/25)+(xp/5)) + (np.exp(-2*xp))/25

plt.plot(xp,yp,'k',label='Exact Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title("Function 1")
plt.show() 

#Question 2
y = [1]
x_sp=(2,3)
xp = np.linspace(x_sp[0],x_sp[1],25,endpoint = False)

sol = solve_ivp(fun_2, x_sp , y,t_eval=xp)
plt.scatter(sol.t,sol.y[0],c='b',label='Using solve_ivp')

yp = xp + (1/(xp-3))

plt.plot(xp,yp,'k',label='Exact Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title("Function 2")
plt.show() 


#Question 3
y = [2]
x_sp=(1,2)
xp = np.linspace(x_sp[0],x_sp[1],25)

sol = solve_ivp(fun_3, x_sp , y,t_eval=xp)
plt.scatter(sol.t,sol.y[0],c='b',label='Using solve_ivp')

yp = 2*xp + xp*np.log(xp)

plt.plot(xp,yp,'k',label='Exact Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title("Function 3")
plt.show() 



#Question 4
y = [1]
x_sp=(0,1)
xp = np.linspace(x_sp[0],x_sp[1],25)

sol = solve_ivp(fun_4, x_sp , y,t_eval=xp)
plt.scatter(sol.t,sol.y[0],c='b',label='Using solve_ivp')

yp = 4/3 - (np.cos(3*xp))/3 + (np.sin(2*xp))/2

plt.plot(xp,yp,'k',label='Exact Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title("Function 4")
plt.show() 









