from scipy.integrate import nquad 
print("18MEC24006-DENNY JOHNSON P")
def f(y,x):
    return x*y**2

def limits_y(x):
    return[0,x]

def limits_x():
    return[1,2]

ans,err= nquad(f,[limits_y,limits_x])
print(round(ans,3))
print("18MEC24006-DENNY JOHNSON P")