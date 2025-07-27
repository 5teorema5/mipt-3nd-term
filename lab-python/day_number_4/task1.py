arr = sorted(map(int, input().split()))
n = int(input())
for i in range(n, 0, -1):
    print(arr[len(arr) - i])
