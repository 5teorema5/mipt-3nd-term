import numpy as np

input_1 = '5 5'
input_2 = '2'
input_3 = ['1 1 1', '4 4 2']

N, M = map(int, input_1.split())
K = int(input_2)

a = np.zeros((N, M), dtype=np.int8)
for i in range(K):
    X, Y, D = map(int, input_3[i].split())
    a[X-D:X+D+1, Y-D:Y+D+1] = 1

print(M * N - a.sum())
