import numpy as np

a = dict()
b = ''
k = int(input())
for i in range(k):
    tmp = input().split()
    a[tmp[0]] = tmp[1:]

p = input().split()

winner = []

for x in p:
    for i in a.keys():
        for j in range(len(a[i])):
            if a[i][j] == x:
                a[i][j] = '0'
                break
    for i in a.keys():
        if a[i] == ['0'] * 15:
            winner.append(i)

    if len(winner) != 0:
        for x in sorted(winner):
            print(x, end=' ')
        break



