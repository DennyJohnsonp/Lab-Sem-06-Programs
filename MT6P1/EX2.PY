import numpy as np 
import sympy as sp 
def is_independent(S):
    alphas=sp.symbols(f'a:{len(S)}')
    M=None
    for i,var in enumerate(alphas):
        if M is None:
            M=var*S[i]
        else:
            M=M+var*S[i]
    soln=sp.solve(M,alphas,manual=True)
    print(soln)
    if np.abs(soln[0]).sum()==0:
        print("the set S is linearly independent")
        return True
    else:
        print("No! its linearly dependent")
        print("and the scalars are", soln)
        return False
def basis(B,dim):
    if is_independent(B):
        if len(B)==int(dim):
            print(f'And the dimension of V={dim}=number of elements in B')
            print('So, the given set is a basis')
            return True
        else:
            print('But, the dimension is not matched, so not a basis')
            return False
    else:
        print('so, not a basis')
        return False
print("18MEC24006-DENNY JOHNSON P")
B=np.array([[1,0,0,-1],[0,1,0,-1],[0,0,1,-1],[0,0,0,1]])
dim=4
basis(B,dim)
x=sp.symbols('x')
B=np.array([1+x+x** 2,x+x** 2,x** 2])
dim=3
basis(B,dim)