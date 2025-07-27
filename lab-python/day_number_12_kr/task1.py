import numpy as np

a = input()
b = ''
for x in a:
    if x in '0123456789':
        b += x
a = int(b[0] + b[-1])
print(a - int(input()))
