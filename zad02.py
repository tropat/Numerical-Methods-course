import numpy as np

n = 30

def gaussseidel(x):
    indexes = [-4,-1,0,1,4]
    b = [1]*128
    for i in range(128):
        sum = b[i]
        for j in range(len(indexes)):
            if i!=indexes[j] and indexes[j] >= 0 and indexes[j] <= 127:
                sum = sum - x[indexes[j]]
            indexes[j] = indexes[j] +1 
        x[i] = sum/4
    return x

norm = np.array([0.0]*n)

def gradientowsprzezonych(x):
    b = np.array([[1.0]*128]).T
    x = np.array([x]).T
    x1 = np.array(x)
    rk = np.array(b)
    pk = np.array(rk)
    for k in range(n):
        indexes = [-4,-1,0,1,4]
        y = np.array([[0.0]*128]).T
        for i in range(128):
            sum = 0
            for j in range(len(indexes)):
                if i!=indexes[j] and indexes[j] >= 0 and indexes[j] <= 127:
                    sum += pk[i][0]
                elif i==indexes[j]:
                    sum += 4*pk[i][0]
                indexes[j] = indexes[j] + 1
            y[i][0] = sum

        ak = np.dot(rk.T,rk)/np.dot(pk.T,y)
        x1 = np.array(x)
        x = (x + (ak*pk))
        norm[k] = np.linalg.norm(x-x1)
        rk1 = rk - (ak*y)
        bk = np.dot(rk1.T,rk1)/np.dot(rk.T,rk)
        pk = rk1 + (bk*pk)
        rk = np.array(rk1)
    return x.T

import matplotlib.pyplot as plt

x = [0]*128
for i in range(5):
    x = gaussseidel(x)
    
print(x)
print(gradientowsprzezonych([0]*128))

z = [i for i in range(n)]
plt.plot(z,norm)

x = [0]*128
norm = [0]*n
for i in range(n):
    y = np.array(x)
    x = gaussseidel(x)
    norm[i] = np.linalg.norm(x-y)


plt.plot(z,norm)
plt.show()

