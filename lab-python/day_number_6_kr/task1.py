n, k, m = map(int, input().split())
D_m = input().split()

flag = True
for i in range(m):
    if int(D_m[i]) == 0: flag = False
    n -= int(D_m[i])
    if n == 0: break
    if flag: n += k
    flag = True

print(n)
