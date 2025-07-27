from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k):
    return k * x


def mnk(x, y):
    n = len(x)
    k = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - (np.mean(x) ** 2))
    b = np.mean(y) - k * np.mean(x)
    sigma_k = 1 / (n ** 0.5) * (
                (np.mean(y ** 2) - np.mean(y) ** 2) / (np.mean(x ** 2) - np.mean(x) ** 2) - k ** 2) ** 0.5
    sigma_b = sigma_k * ((np.mean(x ** 2) - (np.mean(x) ** 2)) ** 2)
    return k, b, sigma_k, sigma_b


T_exp, T_theor = [], []
with open('data_1.txt') as file:
    for s in file:
        T_exp.append(float(s.split()[0]))
        T_theor.append(float(s.split()[1]))

T_exp = np.array(T_exp)
T_theor = np.array(T_theor)

print(mnk(T_exp, T_theor))

coefs, pcov = curve_fit(func, T_theor, T_exp)

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)

plt.figure(dpi=100)
plt.plot(T_theor, T_exp, 'k8', ms=3)

plt.plot(T_theor, func(T_theor, coefs[0]), 'r-', label='approx by mnk')
# plt.title('Теоретические и экспериментальные значения\nпериодов исследуемых колебаний')
plt.xlabel('$T_{theor}$, мкс')
plt.ylabel('$T_{exp}$, мкс')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
# plt.xticks(np.linspace(0, 250, 7))
# plt.yticks(np.linspace(0, 250, 7))
plt.show()
