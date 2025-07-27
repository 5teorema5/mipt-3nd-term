from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


tau = []
D_nu = []

with open('data1.txt', 'r') as file:
    for line in file:
        tau.append(int(line.split()[0]))
        D_nu.append(float(line.split()[1]))

tau = np.array(tau)
x = 1 / tau
D_nu = np.array(D_nu)
y = D_nu

coefs, pcov = curve_fit(func, x, y)

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0] / 1000, 5)}')
plt.xlabel('$1/τ$, 1/мкс')
plt.ylabel('$\Delta ν$, кГц')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')
