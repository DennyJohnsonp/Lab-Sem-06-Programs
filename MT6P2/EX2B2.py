from scipy.integrate import nquad 
print("18MEC24006-DENNY JOHNSON P")
def f(y,x):
    return 1

def limits_y(x):
    return[0,((9-x**2)**0.5)]

def limits_x():
    return[0,3]

ans,err= nquad(f,[limits_y,limits_x])
print(round(ans,3))
print("18MEC24006-DENNY JOHNSON P")