import numpy as np

a = np.array(input().split())
b, c = np.unique(a, return_counts=True)
for i in range(c.max(), 0, -1):
    for j in b[c==i]:
        print(f'{i} {j}')
