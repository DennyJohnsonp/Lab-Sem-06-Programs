import sympy as sp
print("18MEC24006-DENNY JOHNSON P")
x,y,z,t = sp.symbols("x,y,z,t")
a=4
b=3
x=a*sp.cos(t)
y=b*sp.sin(t)


diffx=sp.diff(x,t)
diffy=sp.diff(y,t)

i1=((x+(2*y))*diffx)+((4-(2*x))*diffy)
i=sp.integrate(i1,(t,0,2*sp.pi))
print(i)
print("18MEC24006-DENNY JOHNSON P")