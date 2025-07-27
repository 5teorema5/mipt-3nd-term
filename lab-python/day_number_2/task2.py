def Non_Range(n):
    a = [0] * 8 + [1] + [0] * (n - 9)
    for i in range(9, n):
        a[i] = a[i - 1] + a[i - 2] + a[i - 3] + a[i - 4] + a[i - 5] + a[i - 6] + a[i - 7] + a[i - 8] + a[i - 9]
    return a[n - 1]


n = int(input())
print(Non_Range(n))
