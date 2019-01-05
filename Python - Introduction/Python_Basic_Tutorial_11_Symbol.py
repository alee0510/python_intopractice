# tutorial 11 : symbol
from sympy import *

print("Tutorial 11 : Symbol")

x, y = symbols('x, y')
z = x*y
print(z)

# another example
print("\nsymbol examples")
print(2*x + 3*x - y)                # Algebraic computation
print(diff(x**2, x))                # Differentiates x**2 wrt. x
print(integrate(cos(x), x))         # Integrates cos(x) wrt. x 
print(simplify((x**2+x**3)/x**2))   # Simplifies expression
print(limit(sin(x)/x, x, 0))        # Simplifies expression
print(solve(5*x-15, x))             # Solves 5*x = 15