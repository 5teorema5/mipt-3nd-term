from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


I, U, nu, fi = [], [], [], []

with open('data2.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))
        fi.append(float(line.split()[4]) / float(line.split()[3]))

with open('data3.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))
        fi.append(float(line.split()[4]) / float(line.split()[3]))

nu = np.array(nu)
I = np.array(I) * 10 ** (-3)
U = np.array(U)
psi = np.array(fi) * np.pi - 0.5 * np.pi

x = np.sqrt(nu)
y = psi - np.pi / 4

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

# plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

ax.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}')
plt.ylabel(r'$\psi - \frac{\pi}{4}$')
plt.xlabel(r'$\sqrt{v}$, $Гц^{0.5}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
ax.errorbar(x, y, yerr=[np.sqrt(np.diag(pcov))[1] for i in range(len(x))] , fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image3.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
