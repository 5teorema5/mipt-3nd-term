from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

tau, T = [], []

def func(x, k, b):
    return k * x + b

with open('data.txt', 'r') as file:
    for line in file:
        tau.append(float(line.split()[0]))
        T.append(float(line.split()[1]))

tau = np.array(tau) * 10 ** (-6)
tau_0 = 6.9092 * 10 ** (-6)
T = np.array(T)

x = T
y = 1 / (tau**2 - tau_0**2)

coefs, pcov = curve_fit(func, x, y)

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)

fig, axs = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k.', ms=5, label='Экспериментальные данные')

# plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label='approx by mnk')

plt.ylabel('1/($t^2$ - $t_{o}^2$), 1/$c^2$')
plt.xlabel('$T, C^{\circ}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image2.jpg')
