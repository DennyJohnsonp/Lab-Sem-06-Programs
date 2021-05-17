import sympy as sp
print("18MEC24006-DENNY JOHNSON P")
x,y=sp.symbols("x,y")
y=x**2+1 #change here
diffx=sp.diff(x,x)
diffy=sp.diff(y,x)
i1=(((3*x)+y)*diffx)+(((2*y)-x)*diffy) #change here
i=sp.integrate(i1,(x,0,3))#chnage limits
print(i)
print("18MEC24006-DENNY JOHNSON P")