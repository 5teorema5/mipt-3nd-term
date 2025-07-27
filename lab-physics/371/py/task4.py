from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

nu, L = [], []

with open('data4.txt', 'r') as file:
    for line in file:
        nu.append(float(line.split()[0]) / 1000)
        L.append(float(line.split()[1]))

nu = np.array(nu)
L = np.array(L)

x = nu
y = L


fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

plt.plot(x, y, 'k8', ms=5, label=f'L_min = {min(L)} мГн, L_max = {max(L)} мГн')

plt.ylabel(r'$L, мГн$')
plt.xlabel(r'$\nu, кГц$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image4.jpg')

