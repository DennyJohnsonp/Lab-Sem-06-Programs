from sympy import symbols,expand
import numpy as np
def t(x):
    x1=x[0]
    x2=x[1]
    return np.array([x1,2*x1+x2])
def check_linear(t,no_co_ordinates_input=2):
    x=np.array(symbols(f'x:{no_co_ordinates_input}'))
    y=np.array(symbols(f'y:{no_co_ordinates_input}'))
    c=symbols('c')
    lhs=t(c*x+y)
    rhs=c*t(x)+t(y)
    lhs=[expand(i) for i in lhs]
    print(f't(cx+y) is:{lhs}.')
    rhs=[expand(i) for i in rhs]
    print(f'ct(x)+t(y) is:{rhs}.')
    if lhs==rhs:
        print("18MEC24006-DENNY JOHNSON P")
        print('And ,T(cx+y)=cT(x)+T(y).so the given t is linear')
        return True
    else:
        print("18MEC24006-DENNY JOHNSON P")
        print('And,T(cx+y) is not equal to cT(x)+T(y)so the given t is not linear')
        return False
check_linear(t)
            