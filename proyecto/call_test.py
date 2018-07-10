import numpy as np
import fem3d as fem

va = 1
rho = 1
nu = 1

A = fem.calcA(0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
B = fem.calcB(va, 0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
C = fem.calcC(rho, 0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
D = fem.calcD(nu, 0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
E = fem.calcE(0.5, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

print(A)
print(B)
print(C)
print(D)
print(E)
