import sympy as sp
print("18MEC24006-DENNY JOHNSON P")
x,y=sp.symbols("x,y")
y=x**2
diffx=sp.diff(x,x)
diffy=sp.diff(y,x)
i1=x*diffy-y*diffx
i=sp.integrate(i1,(x,0,1))
print(i)
print("18MEC24006-DENNY JOHNSON P")