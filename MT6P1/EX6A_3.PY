#TYPE 1

from sympy.abc import x, y, a, b, c
from sympy import *
f = Function('f')
u = f(x,y)
p = u.diff(x)
q = u.diff(y)
eq = p*q+p+q  #change for other questions
Eq = eq.subs(p,a).subs(q,b)
print("Equation becomes ",Eq)
b_val=solve(Eq,b)   #finding b in terms of a
print("b = ", b_val)
z = a*x + b*y + c
ans = z.subs(b,b_val[0])
print("18MEC24006-DENNY JOHNSON P")
print("The required solution is ", ans)