import numpy as np
import matplotlib.pyplot as plt

tau, T = [], []

with open('data.txt', 'r') as file:
    for line in file:
        tau.append(float(line.split()[0]))
        T.append(float(line.split()[1]))

tau = np.array(tau) * 10 ** (-6)
tau_0 = 6.9092 * 10 ** (-6)
T = np.array(T)

x = T
y = tau**2 - tau_0**2

fig, axs = plt.subplots(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k.', ms=5, label='Экспериментальные данные')

plt.ylabel('($t^2$ - $t_{o}^2$), $c^2$')
plt.xlabel('$T, C^{\circ}$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')
