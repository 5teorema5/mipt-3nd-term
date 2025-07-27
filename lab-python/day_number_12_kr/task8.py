a = input()
b = ''
d = {'one': 1, 'two': 2, 'three': 3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero': 0}
for i in range(len(a)):
    if a[i] in '0123456789':
        b += a[i]
    tmp = ''
    for j in range(i, len(a)):
        tmp += a[j]
        if tmp in d.keys():
            b += str(d[tmp])


if len(b) >= 2:
    a = int(b[0] + b[-1])
elif len(b) == 1:
    a = int(b[0] + b[0])
else:
    a = 0
print(a - int(input()))