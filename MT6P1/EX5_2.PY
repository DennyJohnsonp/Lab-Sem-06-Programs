from sympy import symbols,simplify,diff
x,y,z = symbols("x,y,z")
P=y*z
Q=2*x*z
R=-3*x*y
f=simplify(P*(diff(Q,z)-diff(R,y))+Q*(diff(R,x)-diff(P,z))+R*(diff(P,y)-diff(Q,x)))
if f==0:
    print("18MEC24006-DENNY JOHNSON P")
    print("Integrable")
else:
    print("18MEC24006-DENNY JOHNSON P")
    print("Not Integrable")