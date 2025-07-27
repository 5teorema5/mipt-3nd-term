from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


I, U, nu = [], [], []

with open('data1.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))

with open('data2.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))

nu = np.array(nu)
I = np.array(I) * 10 ** (-3)
U = np.array(U)

x = nu ** 2
y = 1 / (U / (nu * I)) ** 2

coefs, pcov = curve_fit(func, x, y)

plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}, b = {round(coefs[1], 5)}')
plt.ylabel(r'$1/ξ^{2}$, $\frac{Гц^2}{Ом^2}$')
plt.xlabel('$v^2$, $Гц^2$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
