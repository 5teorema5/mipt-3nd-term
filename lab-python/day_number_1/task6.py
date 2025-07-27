m, n = map(int, input().split())
k = int(input())
flag = True
point_min, point_max = [], []

for i in range(k):
    x1, x2, y1, y2 = map(int, input().split())
    for p in range(len(point_min)):
        if x1 > point_min[p][0] and y1 > point_min[p][1] and x1 < point_max[p][0] and y1 < point_max[p][1]:
            if flag: print('broken')
            flag = False
        if x2 > point_min[p][0] and y2 > point_min[p][1] and x2 < point_max[p][0] and y2 < point_max[p][1]:
            if flag: print('broken')
            flag = False
        if x2 > n or y2 > m:
            if flag: print('broken')
            flag = False
    point_min.append([x1, y1])
    point_max.append([x2, y2])
if flag:
    print('correct')
