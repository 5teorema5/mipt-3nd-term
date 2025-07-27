import numpy as np

a = np.array(list(map(int, input().split())))
b, c = np.unique(a, return_counts=True)
print(b[c==1].max())
