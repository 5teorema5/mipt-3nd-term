n, arr = int(input()), []
for i in range(n):
    tmp = input().split()
    arr.append([tmp[1], tmp[0]])

print(*[x[1] for x in sorted(arr, reverse=True)], sep='\n')