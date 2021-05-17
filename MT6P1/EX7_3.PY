from sympy import*
x,t=symbols('x,t')
u=Function('u')
c=1; sol=0; l=pi; f=x**3; g=0
eq=diff(u,(t,2))-(c**2)*diff(u,(x,2))
for n in range(1,4):
    En=(2/l)*integrate(f*sin((n*pi*x)/l),(x,0,l))
    Fn=(2/n*pi*c)*integrate(g*sin((n*pi*x)/l),(x,0,l))
    sol=sol+(En*cos((n*pi*c*t)/l)+Fn*sin((n*pi*c*t)/l))*sin((n*pi*x)/l)
print(sol)