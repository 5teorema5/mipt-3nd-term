graph = dict()

a = list(map(int, input().split()))
o = len(a)
for x in a:
    graph[x] = []
k = int(input())
for i in range(k):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

main = list(map(int, input().split()))
k = int(input())
a = []
for x in main:
    arr = graph[x] + [x]
    for i in range(1, k):
        for x in set(arr):
            arr += graph[x]
    a += arr

for x in list(set(a)):
    print(x, end=' ')
