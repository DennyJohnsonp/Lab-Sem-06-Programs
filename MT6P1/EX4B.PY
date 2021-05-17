from sympy import *
import numpy as np
a,c1,c2,x,y=symbols('a,c1,c2,x,y')
A=Matrix([[2,3],[4,-5]])
u1=np.array([1,-1])
u2=np.array([1,1])
v1=np.array([1,0])
v2=np.array([0,1])
T0=[A[0,0]*v1,A[1,0]*v2]
T1=[A[0,1]*v1,A[1,1]*v2]
sumT0=T0[0]+T0[1]
sumT1=T1[0]+T1[1]
print('The images of ordered basis vectors in B1 under the transformation are,', sumT0,sumT1)
eq=np.array([u1[0]*c1+u2[0]*c2, u1[1]*c1+u2[1]*c2])
p,q = eq[0], eq[1]
a=solve((p-x,q-y), c1,c2,dict=True)
c1,c2= a[0][c1],a[0][c2]
print('The coordinates of vector (x,y) wrt B1 are ',c1, 'and',c2)
t=sumT0*c1+sumT1*c2
print('The linear transformation of T is T(x,y)=',tuple(t))