from sympy import * 
from sympy.integrals.transforms import laplace_transform,inverse_laplace_transform
from sympy.simplify.fu import L
s,L=symbols('s,L')
t=symbols('t',positive=True)
y0=2
y10=1
Ly2=s**2*L-s*y0-y10
Ly1=s*L-y0
Ly=L
algeq=Eq(Ly2+Ly1-2*Ly,laplace_transform(4,t,s,noconds=True))
print("18MEC24006-DENNY JOHNSON P")
print(algeq)
algsoln=solve(algeq,L)[0]
print(algsoln)
soln=inverse_laplace_transform(algsoln,s,t,noconds=True)
print("Solution:y(t)=",soln)