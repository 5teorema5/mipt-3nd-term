from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

T = np.array([3.703, 3.4, 3.213, 2.775, 2.419, 2.150, 1.825, 1.503, 1.341, 0.804])
N = np.array([12, 11, 10, 9, 8, 7, 6, 5, 4, 3])


def func(x, k, b):
    return k * x + b


x = N
y = T

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

# plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

ax.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.xlabel('Количество шариков')
plt.ylabel('Период колебаний, с')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image2.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
