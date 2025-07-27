import numpy as np

with open('data.txt', 'r') as file:
    N = int(file.readline().split()[0])
    K = np.zeros((2*N, 2*N))
    for i in range(2*N):
        K[i] = list(map(float, file.readline().replace('\n', '').split()))
    f = np.array(list(map(float, file.readline().replace('\n', '').split())))

a = np.linalg.inv(K) @ f
dxs = -a[::2]
anw = max(dxs)
print(f'{np.clip(anw, 0, None):.4f}')