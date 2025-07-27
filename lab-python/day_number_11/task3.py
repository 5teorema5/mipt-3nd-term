import numpy as np

a = np.array(list(map(int, input().split())))
a.sort()
k = int(input())
b = int(np.ceil(k / 100 * a.size))
print(a[b-1])