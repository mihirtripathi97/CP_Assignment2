


import matplotlib.pyplot as plt
import numpy as np

def f(X,t):
    y = np.zeros(2)
    y[0]=X[1]
    y[1]=-10   #np.exp(-2*X[0])
    return y
    
def rk4( f, Y, t ):
    
    n = np.shape(t)[0]
    y = np.zeros((n,len(Y)))
    y[0]=Y
    
    for i in range (n - 1):
        h = t[i+1] - t[i]
        k1 = h * f( y[i], t[i] )
        k2 = h * f( y[i] + 0.5 * k1, t[i] + 0.5 * h )
        k3 = h * f( y[i] + 0.5 * k2, t[i] + 0.5 * h )
        k4 = h * f( y[i] + k3, t[i+1] )
        y[i+1] = y[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0

    return y


def shoot( f, a, b, t, tol ):
    
    
    case = input("For shooting method with secant method press 1 , for use of argmin press 2 : ")
   
    if(case == "1"):
        
        z1=15    #Two initial guess for y' to use secant method
        z2=60
        #z1 = float(input("Enter initial guess for y' : "))
        #z2 = float(input("Enter initial guess for y' : "))
        
        max_iter = 25   # Maximum number of shooting iterations

        n = len( t )    # Determine the size of the arrays we will generate

        Y = [a,z1]
        y = rk4( f, Y , t )
        y_s = [[z1,y[:,0]]]    
        w1 = y[n-1,0]

        print("%2d: z = %10.3e, error = %10.3e" % ( 0, z1, b - w1 ))


        for i in range( max_iter ):

            
            Y = [a,z2]
            y = rk4( f,Y, t )
            y_s.append([z2,y[:,0]])
            w2 = y[n-1,0]

            print("%2d: z = %10.3e, error = %10.3e" % ( i+1, z2, b - w2 ))
   
            if (abs( b - w2 ) < tol):
                break

        
        # new value for z1 is the old value of z2.
        
            z1, z2 = ( z2, z2 + ( z2 - z1 ) / ( w2 - w1 ) * ( b - w2 ) )
            w1 = w2

    

        if (abs( b - w2 ) >= tol):
            print("\a**** ERROR ****")
            print("Maximum number of iterations (%d) exceeded" % max_iter)
            print("Returned values may not have desired accuracy")
            print("Error estimate of returned solution is %e" % ( b - w2 ))

        return y_s,-1

    elif(case == "2"):
        
        z1=30
        z2=90    
        step = 1
        n = len( t )    # Determine the size of the arrays we will generate
        
        while(True):
            #z1 = float(input("Enter initial guess for y' : "))
            #z2 = float(input("Enter initial guess for y' : "))
            #step = float(input("Enter step size for changing the value of y' :"))
            
            Z = np.arange(z1,z2,step)
        
            Y = [a,z1]
            y_s = []
            res = []
            
            for i in range(len(Z)):
                
            
                Y = [a,Z[i]]
                y = rk4( f,Y, t )
                y_s.append([Z[i],y[:,0]])
                res.append(abs(b-y[n-1,0]))
        
            k = np.argmin(res)              #minimum residual indice
            
            if(res[k]<=tol):
                #y_r = [y_s[0],y_s[-1],y_s[k],y_s[k+1],y_s[k-1]]
                #print(y_r)
                print("We get minimum error for y' = ",Z[k]," Error = ",res[k])                      
                return y_s,k
                
                
            
            else:
                print("The residual error between predicted solution and boundry condition is greater then the given tolerence.")
                print("Please enter new guesses of y' and step size: ")
                z1 = float(input("Enter initial guess for y' : "))
                z2 = float(input("Enter initial guess for y' : "))
                step = float(input("Enter step size for changing the value of y' :"))
            
            
        
                
t_initial = 0
t_final = 10.0
y_initial = 0.0
y_final = 0

tol=0.01



t = list(np.linspace(t_initial,t_final,20))


y_t,k = shoot( f, y_initial, y_final, t, tol )  # k is solution indices 
 
#print(y_t)


    
if (k != -1):
    plt.plot(t,y_t[0][1],'g',label="Initial guess Solution, y'(0) = %.1e" %(y_t[0][0]))
    plt.plot(t,y_t[-1][1],'g',label="Final guess Solution, y'(0) = %.1e" %(y_t[-1][0]))            
    
    if len(y_t)>5:
        if(k+1<(len(y_t)-1)):
            plt.plot(t,y_t[k-1][1],'g',label="Step Solution, y'(0) = %.1e " %(y_t[k-1][0]))
            plt.scatter(t,y_t[k][1],c='r',label="Numerical Solution, y'(0) = %.1e" %(y_t[k][0]))
            plt.plot(t,y_t[k+1][1],'g',label="Step Solution, y'(0) = %.1e" %(y_t[k+1][0]))
        
        if(k+1>=(len(y_t)-1)):
            plt.plot(t,y_t[k-1][1],'g',label="Step Solution, y'(0) = %.1e " %(y_t[k-1][0]))
            plt.scatter(t,y_t[k][1],c='r',label="Numerical Solution, y'(0) = %.1e" %(y_t[k][0]))
            plt.plot(t,y_t[k-2][1],'g',label="Step Solution, y'(0) = %.1e" %(y_t[k-2][0]))
    
    if (len(y_t)<=5):
        for i in range (1,len(y_t)-1,1):  
            if i==k:
                pass
            plt.plot(t,y_t[i][1],'g',label="Step Solution, y'(0) = %.1e" %(y_t[i][0]))
        plt.scatter(t,y_t[k][1],c='r',label="Numerical Solution y'(0) = %.1e" %(y_t[k][0]))
        
        
    
else:
    plt.plot(t,y_t[0][1],'g',label="Initial guess Solution, y'(0) = %.1e" %(y_t[0][0]))
    plt.plot(t,y_t[1][1],'g',label="Final guess Solution, y'(0) = %.1e" %(y_t[1][0])) 
    for i in range (2,len(y_t)-1):    
        if i>5:
            break
        plt.plot(t,y_t[i][1],'g',label="Step Solution, y'(0) = %.1e" %(y_t[i][0]))
    plt.scatter(t,y_t[-1][1],c ='r',label="Numerical Solution, y'(0) = %.1e" %(y_t[-1][0]))
    
            

plt.legend()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.title("X(t) vs t")
plt.show() 







