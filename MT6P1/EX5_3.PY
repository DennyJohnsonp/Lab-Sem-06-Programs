from sympy import symbols,simplify,diff
x,y,z = symbols("x,y,z")
P=y**2
Q=(x+z)**2
R=y**2
f=simplify(P*(diff(Q,z)-diff(R,y))+Q*(diff(R,x)-diff(P,z))+R*(diff(P,y)-diff(Q,x)))
if f==0:
    print("18MEC24006-DENNY JOHNSON P")
    print("Integrable")
else:
    print("18MEC24006-DENNY JOHNSON P")
    print("Not Integrable")