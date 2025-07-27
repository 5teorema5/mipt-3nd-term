import numpy as np

input_1 = '4 6'
input_2 = [' 1  4  4  2  1  1',
           ' 0  0  1  0 -1 -1',
           '-2 -3 -1 -5 -6 -4',
           '-1 -3 -3 -4 -4 -2']

N, M = map(int, input_1.split())
a = np.zeros((N, M), dtype=np.int8)
for i in range(N):
    a[i, :] = list(map(int, input_2[i].split()))

print(len(a[a < -5]))
print(-a[a < 0].sum())
print(a.max())
