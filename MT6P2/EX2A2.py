from scipy.integrate import nquad 
import sympy as sp
print("18MEC24006-DENNY JOHNSON P")
def f(x,y):
    return(sp.cos(x)*sp.sin(x))

def limits_y():
    return[0,sp.pi/3]

def limits_x(y):
    return[0,sp.pi/6]

ans,err= nquad(f,[limits_x,limits_y])
print(round(ans,3))
print("18MEC24006-DENNY JOHNSON P")