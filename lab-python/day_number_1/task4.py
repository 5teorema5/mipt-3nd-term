n = int(input())
arr_plus, arr_minus = [], []
for i in range(n):
    new_el = int(input())
    if new_el >= 0:
        arr_plus.append(new_el)
    else:
        arr_minus.append(new_el)
arr_plus = sorted(arr_plus, reverse=False)
if arr_plus:
    print(*arr_plus, end=' ')
arr_minus = sorted(arr_minus, reverse=True)
print(*arr_minus)

