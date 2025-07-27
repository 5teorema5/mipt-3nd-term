path = input()
data = []
n = int(input())
try:
    with open(path, 'r') as file:
        for line in file:
            data.append(line.split())
    data = sorted(data, key = lambda k: float(k[1]), reverse=True)
    for i in range(n):
        print(data[i][0])
except:
    print("Can not read data")