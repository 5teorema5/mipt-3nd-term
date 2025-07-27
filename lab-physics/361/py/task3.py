from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


m = []
a_main = []
a_side = []

with open('data3.txt', 'r') as file:
    for line in file:
        m.append(float(line.split()[0]))
        a_main.append(float(line.split()[2]))
        a_side.append(float(line.split()[1]))

m = np.array(m)
x = m / 100
a_main = np.array(a_main)
a_side = np.array(a_side)
y = a_side / a_main

coefs, pcov = curve_fit(func, x, y)

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}')
plt.xlabel('$m$')
plt.ylabel('$a_{бок}/a_{осн}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image3.jpg')

print(*(a_main*m / 2 / 100), sep='\t')
print(*a_side, sep='\t')
