from sympy.integrals.transforms import  inverse_laplace_transform
from sympy.abc import symbols
t,s=symbols('t,s',positive=True)

ans1=inverse_laplace_transform((1/(s+3)**3),s,t)
print("18MEC24006-DENNY JOHNSON P")
print(ans1)

ans2=inverse_laplace_transform((3*s**2+10*s-6)/s**4,s,t)
print(ans2)

ans3=inverse_laplace_transform(s/(s-3)**5,s,t)
print(ans3)

ans4=inverse_laplace_transform((2*s-11)/(s**2+4*s+8),s,t)
print(ans4)

