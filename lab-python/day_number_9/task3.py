import numpy as np

path_1 = input()
path_2 = input()
X = map(float, input().split())

N = len(X)
A = np.zeros((N, N))
b = np.zeros(N)

with open(path_1) as file:
    for i, line in enumerate(file):
        A[i] = [float(j) for j in line.split()]

with open(path_1) as file:
    b[0:N] = [float(j) for j in file.read().split()]

print((A @ X) @ b)
