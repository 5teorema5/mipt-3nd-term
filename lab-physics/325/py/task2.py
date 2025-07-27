from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


t = []
r = []

with open("data3.txt") as file:
    for f in file:
        t.append(float(f.split()[0]))
        r.append(float(f.split()[1]))


x = 1 / np.array(r) ** 2
y = 1 / np.array(t) ** 2

coefs, pcov = curve_fit(func, x, y)

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=3)

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label='approx by mnk')
# plt.title('Теоретические и экспериментальные значения\nпериодов исследуемых колебаний')
plt.xlabel('1 / R^{2}, 1 / $Om^{2}$')
plt.ylabel('1 / $O^{2}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
plt.show()
