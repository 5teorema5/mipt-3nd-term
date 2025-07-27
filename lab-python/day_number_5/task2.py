m, n = map(int, input().split())
p = [0] * n
for i in range(n):
    p[i] = [0] * m
c = 0
s = n * m
K = int(input())
for i in range(K):
    x, y, d = map(int, input().split())
    for j in range(x - d, x + d + 1):
        for k in range(y - d, y + d + 1):
            try:
                p[k][j] = 1
            except:
                pass

for i in range(m):
    for j in range(n):
        if p[j][i] == 0:
            c += 1
print(c)
