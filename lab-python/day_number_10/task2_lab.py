import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

with open('doc/data2.txt', 'r') as file:
    n = int(file.readline().split()[0])
    A = np.zeros((n, n))
    for i in range(n):
        A[i, :] = np.array(file.readline().split())
    b = np.array(file.readline().split())

x = linalg.solve(A, b)
print("Решение СЛАУ: x =", x)

fig, axs = plt.subplots()
axs.bar(range(x.size), x)
axs.grid()
axs.set_title('Решение СЛАУ')

plt.savefig('doc/decision_2.png')
