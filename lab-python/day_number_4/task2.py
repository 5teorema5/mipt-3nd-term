arr, s = map(str, input().split()), 0
for x in arr:
    try:
        s += int(x)
    except:
        pass
print(s)
