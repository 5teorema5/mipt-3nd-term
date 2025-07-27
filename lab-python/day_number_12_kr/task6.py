import numpy as np

N, M = map(int, input().split())
a = np.zeros((N, M), dtype=np.int8)
for i in range(N):
    a[i, :] = list(map(int, input().split()))
c = np.where(a == a.max())[0]
tmp = np.zeros((N+2, M+2), dtype=np.int8)
tmp[1:-1, 1:-1] = a
x = tmp[c[0]+1:c[0]+4, c[1]+1:c[1]+4]
x[1:2, 1:2] = 0
x[1:2, 1:2] = x.max()
print(a.max()-np.clip(x.min(), 0, None))