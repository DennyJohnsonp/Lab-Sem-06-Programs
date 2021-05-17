import sympy as sp
print("18MEC24006-DENNY JOHNSON P")
x,y,z,t = sp.symbols("x,y,z,t")
x=sp.exp(t)
y=sp.exp(-t)
z=t**2

diffx=sp.diff(x,t)
diffy=sp.diff(y,t)
diffz=sp.diff(z,t)
i1=x*y*diffx + (x**2)*z*diffy + x*y*z*diffz
i=sp.integrate(i1,(t,0,1))
print(i)
print("18MEC24006-DENNY JOHNSON P")
