from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


I, B = [], []


with open('data.txt', 'r') as file:
    for line in file:
        I.append(float(line.split()[0]))
        B.append(round(abs(float(line.split()[2])-float(line.split()[1]))/0.0072/1000, 3))

I = np.array(I)
B = np.array(B)

x = I
y = B

coefs, pcov = curve_fit(func, x, y)

plt.figure(dpi=80, figsize=(10, 6))
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(x, func(x, coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)} Тл/А')
plt.ylabel(r'$B, Тл$')
plt.xlabel(r'$I, А$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')

coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)
