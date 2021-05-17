
from sympy import *
x,t=symbols ('x,t') 
u=Function ("u")
c=4; sol=0;l=1; f=x**2-x
eq=diff(u,t)-(c**2)*diff(u, (x, 2))
for n in range(4) :
    Bn=2*integrate (f*sin(n*pi*x),(x, 0,1))
    sol=sol+(Bn*sin((n*pi*x)/1)*exp(((-c**2*n**2*pi**2)/1**2) *t))
print ("solution3=",sol)