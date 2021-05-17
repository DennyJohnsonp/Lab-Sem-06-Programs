from sympy import *
import numpy as np
x,y,z,a,b,c=symbols("x,y,z,a,b,c")
F=np.array([x**2-y*z,y**2-x*z,z**2-y*x])

#Computing the LHS
G = diff(F[0],x)+diff(F[1],y)+diff(F[2],z)
LHS=simplify(integrate(G,(z,0,c),(y,0,b),(x,0,a)))
print("The left hand side of Gauss Divergence Theorem formula is,",LHS)

#Computing the RHS
i=np.array([1,0,0])
j=np.array([0,1,0])
k=np.array([0,0,1])

s1=np.dot(F,i)
I1=integrate(s1.subs(x,a),(y,0,b),(z,0,c))
print("I1 is ",I1)

s2=np.dot(F,j)
I2=integrate(s2.subs(y,b),(x,0,a),(z,0,c))
print("I2 is",I2)

s3=np.dot(F,k)
I3=integrate(s3.subs(z,c),(x,0,a),(y,0,b))
print("I3 is",I3)

s4=np.dot(F,-i)
I4=integrate(s4.subs(x,0),(y,0,b),(z,0,c))
print("I4 is",I4)

s5=np.dot(F,-j)
I5=integrate(s5.subs(y,0),(x,0,a),(z,0,c))
print("I5 is",I5)

s6=np.dot(F,-k)
I6=integrate(s6.subs(z,0),(x,0,a),(y,0,b))
print("I6 is",I6)

RHS=simplify(I1+I2+I3+I4+I5+I6)
print("The Right hand side of Gauss Divergence Theorem formula is,",RHS)

if RHS==LHS:
    print("18MEC24006-DENNY JOHNSON P")
    print("Gauss divergence theorem is verified")
else:
    print("Gauss divergence theorem is not verified")