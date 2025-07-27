import numpy as np

A, B, C = [], [], []
with open('dat/data1.txt', 'r') as file:
    for line in file:
        A.append(np.array([int(x) for x in line.split()]))

A = np.array(A)

with open('dat/data2.txt', 'r') as file:
    for line in file:
        B.append(np.array([float(x) for x in line.split()]))

B = np.array(B)

with open('dat/data3.txt', 'r') as file:
    for line in file:
        C.append(np.array([float(x) for x in line.split()]))

C = np.array(C)

for i in range(int(input())):
    A_1 = B@A
    A_2 = C@A.transpose()
    A_3 = A_1 + A_2
    A = np.trunc(A_3)

print(int(A.min()), int(A.max()))

