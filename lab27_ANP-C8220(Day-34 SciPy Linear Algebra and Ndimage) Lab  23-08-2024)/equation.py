#Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10


import numpy as np
from scipy.linalg import solve

# Coefficient matrix A
A = np.array([[7, 2],
              [4, 5]])

# Right-hand side vector B
B = np.array([8, 10])

# Solve the system of equations
solution = solve(A, B)
print(solution)


#Output

[0.74074074 1.40740741]
