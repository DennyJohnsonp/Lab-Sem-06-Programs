from scipy.integrate import nquad 
print("18MEC24006-DENNY JOHNSON P")
def f(y,x):
    return x**2+y

def limits_y(x):
    return[x,x**2]

def limits_x():
    return[0,1]

ans,err= nquad(f,[limits_y,limits_x])
print(round(ans,3))
print("18MEC24006-DENNY JOHNSON P")