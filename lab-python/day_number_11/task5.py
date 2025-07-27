import numpy as np

N = int(input())
x = np.array(list(map(float, input().split())))
A = np.zeros((N, N))
for i in range(N):
    A[i] = list(map(float, input().split()))
k = int(input())

for _ in range(k):
    x = A @ x

for i in range(N):
    print(f'{x[i]:.4f}', end=' ')

