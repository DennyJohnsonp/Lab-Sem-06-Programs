import sympy as sp
from sympy.abc import t,s
from sympy import cos,sin,exp
f=(exp(-3*t)*sin(4*t))
u=sp.laplace_transform(f,t,s,noconds=True)
print("18MEC24006-DENNY JOHNSON P")
print("The Laplcae Transform of the Given Function is:",u)
