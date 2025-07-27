m, s = input().split(), []
for x in m:
    try:
        with open(x) as file:
            s.append([a for b in [p.split() for p in file] for a in b])
    except:
        pass
print(*sorted([x for x in set([a for b in [x for x in s] for a in b])]))
