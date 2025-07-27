from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


I = []
U = []

with open('data1.txt', 'r') as file:
    for line in file:
        I.append(float(line.split()[0]))
        U.append(float(line.split()[1]))

I = np.array(I)
U = np.array(U) * 10
x = U
y = I

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

coefs, pcov = curve_fit(func, x[-6:], y[-6:])
plt.plot(x[-10:], func(x[-10:], coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)} мА/В')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

coefs, pcov = curve_fit(func, x[2:5], y[2:5])
plt.plot(x[:8], func(x[:8], coefs[0], coefs[1]), 'g-', label=f'k = {round(coefs[0], 5)} мА/В')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

plt.xlabel('U, В')
plt.ylabel('I, мА')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')

I = []
U = []

with open('data2.txt', 'r') as file:
    for line in file:
        I.append(float(line.split()[0]))
        U.append(float(line.split()[1]))

I = np.array(I)
U = np.array(U) * 10
x = U
y = I

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5, label='Экспериментальные данные')

coefs, pcov = curve_fit(func, x[-6:-2], y[-6:-2])
plt.plot(x[-10:], func(x[-10:], coefs[0], coefs[1]), 'r-', label=f'k = {round(coefs[0], 5)} мА/В')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

coefs, pcov = curve_fit(func, x[2:5], y[2:5])
plt.plot(x[:8], func(x[:8], coefs[0], coefs[1]), 'g-', label=f'k = {round(coefs[0], 5)} мА/В')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)

plt.xlabel('U, В')
plt.ylabel('I, мА')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image2.jpg')
