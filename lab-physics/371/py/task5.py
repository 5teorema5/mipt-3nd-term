from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


nu, L = [], []
L_max = 9.99
L_min = 2.88 - 0.01

with open('data4.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]) / 1000)
        L.append(float(line.split()[1]))

nu = np.array(nu)
L = np.array(L)

x = (nu ** 2)[:9]
y = ((L_max - L) / (L - L_min))[:9]

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

# plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

ax.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}')
plt.ylabel(r'$(L_max - L)/(L - L_min)$')
plt.xlabel(r'$\nu^2, кГц^2$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
ax.errorbar(x, y, yerr=[np.sqrt(np.diag(pcov))[1] for i in range(len(x))] , fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image5.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
