import numpy as np 
import sympy as sp 

def is_in_span(vector,Set):
    variables= sp.symbols(f'c:{len(Set)}')
    m=-vector
    for i,var in enumerate(variables):
        m=m+var*Set[i]
    scalars=sp.solve(m,variables,dict=True)
    if len(scalars)==0:
        return(f'No.! The given vector{vector}is not in the span of {Set}')
        return False
    else:
        print(f'Yes .! The given vector{vector}is in the span of {Set}')
        print(f'And the Scalars are',scalars[0])
        return scalars
    
v=np.array((2,-1,1))
s=np.array([(1,0,2),(-1,1,1)])
is_in_span(v,s)
print("//////////////////////////////////////")
print("2nd Problem 18MEC24006-DENNY JOHNSON P")
print("//////////////////////////////////////")
a1=[[1,0],[-1,0]]
a2=[[0,1],[0,1]]
a3=[[1,1],[0,0]]
b=sp.Matrix([[1,2],[-3,4]])
c=np.array([a1,a2,a3])
is_in_span(b,c)
