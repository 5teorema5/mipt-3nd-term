path = input()
class_, power_ = map(str, input().split())
c = 0
arr = []
with open(path, 'r') as file:
    for line in file:
        name, arr_class, power = line.split()
        if class_ in arr_class and power >= power_:
            arr.append([name, power])

arr = sorted(arr, key=lambda x: x[1], reverse=True)
for x in arr:
    print(x[0])
