n = int(input())
m = int(input())
a_dict, a_arr, a = dict(), [], []
k = 0

for i in range(m):
    a_arr.append(input().split())

b_tmp = input().split()

X = input().split()

for i in range(m):
    a.append([((float(X[0]) - float(a_arr[i][0])) ** 2 + (float(X[1]) - float(a_arr[i][1])) ** 2 + (
            float(X[2]) - float(a_arr[i][2])) ** 2) ** 0.5, int(b_tmp[i])])

a = sorted(a, reverse=False, key=lambda k: k[0])[:n]

for x in a:
    k += x[1]

if k / 3 >= 0.5:
    print('elephant')
else:
    print('hippopotamus')
