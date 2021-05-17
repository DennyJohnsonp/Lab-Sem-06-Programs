from sympy.abc import x, y, a, b, c,k,p,q
from sympy import cos,sin
from sympy import *
lhs=p-(sin(x)) #change for other questions
rhs=(sin(y))-q  #change for other questions
r1=Eq(lhs , k)
r2=Eq(rhs , k)
h1=solve(r1,p)
h2=solve(r2,q)
print("p =",h1 ,"and","q =",h2)
z=integrate(h1[0],x)+integrate(h2[0],y)
print("18MEC24006-DENNY JOHNSON P")
print("The solution is",z)