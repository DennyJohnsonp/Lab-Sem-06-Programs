import sympy as sp
from sympy.abc import t,s
from sympy import cos
f=(cos(3*t))**2
u=sp.laplace_transform(f,t,s,noconds=True)
print("18MEC24006-DENNY JOHNSON P")
print("The Laplcae Transform of the Given Function is:",u)
