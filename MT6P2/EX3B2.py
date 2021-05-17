from scipy.integrate import nquad 
from numpy import exp
print("18MEC24006-DENNY JOHNSON P")

def f(z,y,x):
    return(x*y)

def limits_z(x,y):
    return[0,(x+y)]

def limits_y(x):
    return[x**2,x**0.5]

def limits_x():
    return[0,1]

ans,err= nquad(f,[limits_z,limits_y,limits_x])
print(round(ans,3))
print("18MEC24006-DENNY JOHNSON P")