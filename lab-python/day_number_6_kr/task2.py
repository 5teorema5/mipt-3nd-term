s = [x.lower() for x in input().split()]
len_max = 0

for x in s:
    if x == x[::-1]:
        len_max = max(len_max, len(x))

print(len_max)
