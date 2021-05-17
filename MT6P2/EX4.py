print("18MEC24006-DENNY JOHNSON P")
from sympy import *
import numpy as np
from sympy import integrate
x,y=symbols("x,y")
def p(x,y):
    return (3*(x*2)-8*(y**2))
dp=diff(p(x,y),y)
def q(x,y):
    return 4*y-6*x*y
dq=diff(q(x,y),x)
s=dq-dp
z1=integrate(s,(y,0,2),(x,0,1))
print(z1)
F=np.array([p(x,y),q(x,y)])
x1=1
dx=diff(x1,x)
dy=diff(y,y)
dt1=np.array([dx,dy])
H1=np.dot(F,dt1)
H11=H1.subs(x,1)
I1=integrate(H11,(y,0,2))
print(I1)
x2=0
dx=diff(x2,x)
dy=diff(y,y)
dt2=np.array([dx,dy])
H2=np.dot(F,dt2)
H22=H2.subs(x,0)
I2=integrate(H22,(y,2,0))
print(I2)
y1=0
dx=diff(x,x)
dy=diff(y1,x)
dt3=np.array([dx,dy])
H3=np.dot(F,dt3)
H33=H3.subs(y,0)
I3=integrate(H33,(x,0,1))
print(I3)
y2=2
dx=diff(x,x)
dy=diff(y2,y)
dt4=np.array([dx,dy])
H4=np.dot(F,dt4)
H44=H4.subs(y,2)
I4=integrate(H44,(x,1,0))
print(I4)
z=I1+I2+I3+I4
print(z)
if z==z1:
    print("Greens theorem is verified")
    print("18MEC24006-DENNY JOHNSON P")
else:
    print("Greens theorem is not verified")
    print("18MEC24006-DENNY JOHNSON P")