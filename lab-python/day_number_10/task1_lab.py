import numpy as np
from sympy import *


rho, lambd, mu = symbols('r l m')

M_3x3 = np.zeros((3, 3))
A = np.diag(np.full(3, -1 / rho))
B = np.diag([-(lambd + 2 * mu), -mu, -mu])
C = np.block([[-lambd, 0, 0], [0, 0, 0], [-lambd, 0, 0]])
I = np.block([[M_3x3, A, M_3x3],
              [B, M_3x3, M_3x3],
              [C, M_3x3, M_3x3]],)

I = Matrix(I)
values = list(I.eigenvals().keys())

print(values)
