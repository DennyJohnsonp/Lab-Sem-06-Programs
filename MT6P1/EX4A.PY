import numpy as np
from numpy import linalg as la

def T(x,y,z):
    return[x-y+z,2*x+3*y-(1/2)*z,x+y-2*z]

b1=np.array([[-1,1,0],[5,-1,2],[1,2,1]])
print("The Specified Basis for thr Domain Space is",b1)


b2=np.array([[1,1,0],[0,0,1],[1,5,2]])
print("The Specified Basis for thr Domain Space is",b2)

w1=T(-1,1,0)
w2=T(5,-1,2)
w3=T(1,2,1)

print("Evaluating T at the vectors of the basis B1:",w1,w2,w3)
v1=la.solve(b2.T,w1)
v2=la.solve(b2.T,w2)
v3=la.solve(b2.T,w3)
m=np.array([v1,v2,v3])
print("The Matrix of the Linear Transformation is:\n",m.T)
