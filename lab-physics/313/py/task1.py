from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

M = np.array([584.913, 532.846, 448.321, 355.681, 238.022])
N = np.array([12, 10, 8, 6, 4])


def func(x, k, b):
    return k * x + b


x = N
y = M

coefs, pcov = curve_fit(func, x, y)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

# plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

ax.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)}')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.xlabel('Количество шариков')
plt.ylabel('Момент сил, дин см')
plt.grid()
plt.legend()

plt.savefig('image1.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
