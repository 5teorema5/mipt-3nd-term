from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


I, U, nu, fi = [], [], [], []
delta_fi = np.tan(np.array([
    0.999090909090909,
    0.885641025641026,
    0.807428571428572,
    0.686875,
    0.757931034482759,
    0.724615384615385,
    0.546086956521739,
    0.418666666666667,
    0.285454545454545,
    0.19625,
    0.112142857142857,
    0.0654166666666667,
    0.0327083333333333,
    0.02453125,
    0.0123
]) * np.pi - 0.5 * np.pi)

with open('data2.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))
        fi.append(float(line.split()[4]) / float(line.split()[3]))

nu = np.array(nu)
I = np.array(I) * 10 ** (-3)
U = np.array(U)
psi = np.array(fi) * np.pi - 0.5 * np.pi

x = nu[:-2]
y = np.tan(psi)[:-2]
# y = delta_fi[1:]

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))
#
# plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

ax.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}')
plt.ylabel(r'$tg \psi$')
plt.xlabel('$v$, $Гц$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
ax.errorbar(x, y, yerr=[np.sqrt(np.diag(pcov))[1] for i in range(13)] , fmt='.', linewidth=2, capsize=6)
plt.legend()

plt.savefig('image2.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
