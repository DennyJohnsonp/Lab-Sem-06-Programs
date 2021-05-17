#TYPE 2

from sympy import Function, diff, solve, dsolve,pprint
from sympy.abc import x, y, u, p, q, a, b
z = Function("z")(u)
eqn=p*(1+q)-(q*z)  #change for other questions
eqn1=eqn.subs(p,diff(z,u)).subs(q,a*diff(z,u))
print(eqn1) 
h1=solve(eqn1,diff(z,u))
print(h1) 
sol=dsolve(h1[0]-diff(z,u))
pprint(sol) 
ans=sol.subs(u,x+a*y)
print("18MEC24006-DENNY JOHNSON P")
print("Required answer is")
print(ans)