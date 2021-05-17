#type 4

from sympy.abc import x, y, a, b, p, q
from sympy import *
z=p*x+q*y+log(p*q)  #change for other questions
sol=z.subs([(p,a),(q,b)])
print("18MEC24006-DENNY JOHNSON P")
print("General solution is ",sol)