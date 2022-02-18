import numpy as np

def thomas(a,d):
    n = len(a)
    b = np.array(a, float)
    c = np.array(d, float)
    x = [0.0]*n
    for k in range(1, n):
        t = b[k][k-1]/b[k-1][k-1]
        b[k][k] = b[k][k] - t*b[k-1][k]
        c[k] = c[k] - t*c[k-1]
    x[n-1] = c[n-1]/b[n-1][n-1]
    for k in range(2, n+1):
        x[n-k] = (c[n-k] - b[n-k][n-k+1]*x[n-k+1])/b[n-k][n-k]
    return x

def func(x):
    return 1/(1+5*x*x)

x = list()
for i in range(0, 33):
    x.append(-1 + i*(1/32))
    if i != 32:
        x.append(1 - i*(1/32))

x.sort()
y = [func(i) for i in x]

h = x[1]-x[0]

n = len(y)

a = np.zeros((n-2,n-2))
indexes = [-1,0,1]
for i in range(n-2):
    for j in range(len(indexes)):
        if i!=indexes[j] and indexes[j] >= 0 and indexes[j] <= n-3:
            a[i][indexes[j]] = 1
        elif i==indexes[j]:
            a[i][indexes[j]] = 4
        indexes[j] = indexes[j] + 1

b = [0]*(n-2)
for i in range(0,n-2):
    b[i] = (6/(h*h))*(y[i] - 2*y[i+1]+y[i+2])

e = thomas(a,b)

e = ([0] + e + [0])

def spline(x0):
    j = 0
    for k in range(0,n-1):
        if x0 >= x[k] and x0 <=x[k+1]:
            j = k
            break

    a = (x[j+1]-x0)/(x[j+1]-x[j])
    b = (x0-x[j])/(x[j+1]-x[j])
    c = (1/6)*(a*a*a-a)*np.power(x[j+1]-x[j], 2)
    d = (1/6)*(b*b*b-b)*np.power(x[j+1]-x[j], 2)

    return a*y[j]+b*y[j+1]+c*e[j]+d*e[j+1]

import matplotlib.pyplot as plt

t = [0.01*i for i in range(-100,100)]
w = [spline(i) for i in t]

plt.plot(t,w)
plt.show()