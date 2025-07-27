from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


nu0 = 50  # кГц

n = []
a_n = []
a_n0 = []

with open('data4.txt', 'r') as file:
    for line in file:
        n.append(float(line.split()[0]))
        a_n.append(float(line.split()[1]))
        a_n0.append(float(line.split()[2]))

n = np.array(n)
x = 1 / (nu0 * n * 10000)
a_n = np.array(a_n)
a_n0 = np.array(a_n0)
y = a_n / a_n0

print(y)

coefs, pcov = curve_fit(func, x, y)

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

coefficients = np.polyfit(x, y, 1)
x = np.linspace(0, 0.000005)
y = np.polyval(coefficients, x)

plt.plot(x, y, 'r', ms=5, label=f'k = {round(coefs[0], 5)}, tau = {round(1 / coefs[0], 10)} c')

plt.xlabel('$1/nv_0$, 1/c')
plt.ylabel('$K = a_{n}/a_{n}^{0}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.show()

plt.savefig('image4.jpg')
