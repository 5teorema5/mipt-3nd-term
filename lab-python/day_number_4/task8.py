from pprint import pprint

n, a_dict = int(input()), dict()

for i in range(n):
    tmp = input().split()
    if tmp[1] == 'SET':
        if int(tmp[0]) + 1 in a_dict.keys():
            a_dict[int(tmp[0]) + 1][tmp[2]] = tmp[3]
        else:
            if len(a_dict.keys()) == 0:
                a_dict[int(tmp[0]) + 1] = {tmp[2]: tmp[3]}
            else:
                p = a_dict[max(a_dict.keys())].copy()
                p[tmp[2]] = tmp[3]
                a_dict[int(tmp[0]) + 1] = p

    else:
        p = a_dict[max(a_dict.keys())].copy()
        del p[tmp[2]]
        a_dict[int(tmp[0]) + 1] = p

pprint(a_dict)

m = int(input())
for i in range(m):
    t = int(input())
    if len(a_dict.keys()) == 0:
        print('(none)')
    elif t < min(a_dict.keys()):
        print('(none)')
    else:
        while t not in a_dict.keys():
            t -= 1
        if len(a_dict[t].keys()) == 0:
            print('(none)')
        else:
            a_keys = sorted(a_dict[t].keys())
            s = f''
            for x in a_keys:
                s += f'{x} : {a_dict[t][x]}, '
            print(s[:-2])
