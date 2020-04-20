


#This code is created with help of Chintan Patel

import numpy as np
from matplotlib import pyplot as plt


def gauss_siedel(A,b):
    x0 = np.zeros(len(b))
    X = [x0]
    k = 0
    while (max(abs(np.dot(A,X[k])-b))>.01):
        
        k = k+1
        x=np.zeros(len(b))
        
        for i in range(len(b)):
            x[i] = X[k-1][i]
            
        for j in range(len(b)):
            s=0
            for l in range(len(b)):
                if (j!=l):
                    s = s + A[j][l]*x[l]
                x[j] = (b[j]-s)/A[j][j]
        X.append(x)
    return(X,k)

g = 10
n = 30    
h = 10/(n-1)
t=np.linspace(0,10,n)

A=np.zeros((n-2,n-2))
A[0,0:2] = [-2,1]
A[n-3,n-4:n-2] = [1,-2]

for i in range(1,n-3):
    A[i,i-1:i+2]=[1,-2,1]
b=[]


for i in range(n-2):
    b.append(-g*h**2)

    
x=np.zeros([n,5])
k=gauss_siedel(A,b)[1]

x_ext=-5*(t**2-10*t)

x[1:n-1,0] = gauss_siedel(A,b)[0][int(k/5)]
x[1:n-1,1] = gauss_siedel(A,b)[0][int(2*k/5)]
x[1:n-1,2] = gauss_siedel(A,b)[0][int(3*k/5)]
x[1:n-1,3] = gauss_siedel(A,b)[0][int(4*k/5)]
x[1:n-1,4] = gauss_siedel(A,b)[0][int(k/2)]
x[1:n-1,4] = gauss_siedel(A,b)[0][k]


print('Solution:\n x = ',x[:,4]) 

plt.plot(t,x_ext,'r',label='Exact solution')
plt.scatter(t,x[:,4],label='Numerical Solution',c='k')

for i in range(5):
    plt.plot(t,x[:,i],'g')

plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.show()    

   







