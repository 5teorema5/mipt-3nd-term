def Fib_Range(n):
    a = [0] + [1] + [0] * (n - 2)
    for i in range(2, n):
        a[i] = a[i - 1] + a[i - 2]
    return a[n-1]


n = int(input())
print(Fib_Range(n))
