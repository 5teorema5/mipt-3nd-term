import numpy as np
import matplotlib.pyplot as plt

I, U, nu = [], [], []

with open('data1.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))

with open('data2.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))

with open('data3.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]))
        I.append(float(line.split()[1]))
        U.append(float(line.split()[2]))

nu = np.array(nu)
I = np.array(I) * 10 ** (-3)
U = np.array(U)

xi = U / (nu * I)
xi_0 = 13.99 * 10 ** (-3)

x = nu
y = xi / xi_0

fig, axs = plt.subplots(dpi=80, figsize=(10, 6))
plt.xscale("log")
plt.plot(x, y, 'k4', ms=5, label='Экспериментальные данные')

sigma = (5.077 + 4.49) / 2 * 10 ** 7
mu0 = 1.256 * 10 ** (-6)
h = 1.5 * 10 ** (-3)
a = 22.5 * 10 ** (-3)
alpha = np.array([np.sqrt(complex(0, 2 * np.pi * sigma * mu0 * x)) for x in nu])
h1h0 = 1 / (np.cosh(h * alpha) + 0.5 * a * alpha * np.sinh(0.4 * h * alpha))

x = nu
y = np.array([(x.real**2 + x.imag**2) for x in h1h0])

plt.plot(x, y, 'r3', ms=5, label='Теоретические данные')

plt.ylabel(r'$\frac{|H_1|}{|H_0|}$')
plt.xlabel('$v$, $Гц$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image6.jpg')
