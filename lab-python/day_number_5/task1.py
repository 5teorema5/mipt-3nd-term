s = input().split('#')
a = [len(x) for x in s]
print(s[a.index(max(a))])
