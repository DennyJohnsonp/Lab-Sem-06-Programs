
from sympy import * 
x,t=symbols('x,t') 
u=Function('u') 
c=0.5; sol=0;l=1; 
eq=diff(u,t)-(c**2)*diff(u,(x,2)) 
for n in range (4): 
    Bn=2*integrate(3*sin(n*pi*x)*sin(n*pi*x),(x,0,1)) 
    sol=sol+(Bn*sin((n*pi*x)/l)*exp(((-c**2*n**2*pi**2)/l**2)*t)) 
print (sol)