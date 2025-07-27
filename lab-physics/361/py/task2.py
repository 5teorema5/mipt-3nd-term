from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


T = []
d_nu = []

with open('data2.txt', 'r') as file:
    for line in file:
        T.append(int(line.split()[0]))
        d_nu.append(float(line.split()[1]))

T = np.array(T)
x = 1 / T
d_nu = np.array(d_nu)
y = d_nu

coefs, pcov = curve_fit(func, x, y)

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0] / 1000, 5)}')
plt.xlabel('$1/T$, 1/мкс')
plt.ylabel('$\delta ν$, кГц')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image2.jpg')
