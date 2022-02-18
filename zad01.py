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

def shermanmorrison(a, b):
    u = np.array([1,0,0,0,0,0,1],float)
    z = np.array([thomas(a,b)]).T
    q = np.array([thomas(a, u)]).T
    x = (z - ((np.dot(u,z) / (1 + np.dot(u,q)))* q))
    return x.T

a = [[4,1,0,0,0,0,0],[1,4,1,0,0,0,0],[0,1,4,1,0,0,0],[0,0,1,4,1,0,0],[0,0,0,1,4,1,0],[0,0,0,0,1,4,1],[0,0,0,0,0,1,4]]
b = [1,2,3,4,5,6,7]

c = [[3,1,0,0,0,0,0],[1,4,1,0,0,0,0],[0,1,4,1,0,0,0],[0,0,1,4,1,0,0],[0,0,0,1,4,1,0],[0,0,0,0,1,4,1],[0,0,0,0,0,1,3]]

print(thomas(a,b))
print(shermanmorrison(c,b))