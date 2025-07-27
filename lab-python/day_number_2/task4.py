m = sorted(map(int, input().split()), reverse=True)
for x in m:
    if m.count(x) == 1:
        print(x)
        break
