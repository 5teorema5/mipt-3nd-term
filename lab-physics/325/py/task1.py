from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


n = []
r = []

with open("data2.txt") as file:
    for f in file:
        n.append(float(f.split()[0]))
        r.append(float(f.split()[1]))


n = np.array(n)
r = np.array(r)

coefs, pcov = curve_fit(func, n, r)

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
print((coef_error[0] ** 2 + coef_error[1] ** 2) ** 0.5)

plt.figure(dpi=100)
plt.plot(n, r, 'k8', ms=3)

plt.plot(n, func(n, coefs[0], coefs[1]), 'r-', label='approx by mnk')
# plt.title('Теоретические и экспериментальные значения\nпериодов исследуемых колебаний')
plt.xlabel('Частота генератора колебаний, Гц')
plt.ylabel('Активное сопротивление магазина индуктивности, Ом')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
plt.show()

print(func(100, coefs[0], coefs[1]))
