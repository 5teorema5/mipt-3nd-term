x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())
z1, z2 = map(float, input().split())
n, count = int(input()), 0

for i in range(n):
    x, y, z = map(float, input().split())
    if (x2 >= x >= x1) and (y2 >= y >= y1) and (z2 >= z >= z1):
        count += 1

print(count)
