D, N = map(float, input().split())
data = [int(float(x) > D) for x in input().split()]
data.append(0)
arr = [0] * len(data)
start = -1
c = 0
for i in range(len(data)):
    if data[i] != 0 and start < 0:
        arr[i] = 's'
        start = i
    elif data[i] == 0 and start >= 0:
        arr[i] = 'f'
        start = -1

print(*arr)