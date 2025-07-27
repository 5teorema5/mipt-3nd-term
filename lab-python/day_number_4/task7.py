from pprint import pprint

n = int(input())
a = []
a_dict = dict()

for i in range(n):
    a.extend(input().split())

for x in a:
    a_dict[x.lower()] = set()

for x in a:
    a_dict[x.lower()].add(x)

a_ = sorted(a_dict, reverse=True, key=lambda k: len(a_dict[k]) or k)

for x in a_:
    if len(a_dict[x]) > 2: print(x)
