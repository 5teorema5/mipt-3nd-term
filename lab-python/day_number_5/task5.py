D, N = map(float, input().split())
data = [float(x) for x in input().split()]
data.append(0)
c = 0
for i in range(len(data)):
    data[i] = 0 if data[i] < D else data[i]
start = -1
print(*data)
for i in range(len(data)):
    if data[i] != 0 and start == -1:
        start = i
    if data[i] == 0 and start >= 0 and (i - start >= N):
        c += 1
        start = -1
print(c)
