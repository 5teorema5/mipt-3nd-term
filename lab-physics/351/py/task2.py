from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


I = []
U = []

with open('data3.txt', 'r') as file:
    for line in file:
        U.append(float(line.split()[0]))
        I.append(float(line.split()[1]))

I = np.array(I) - I[-1]
U = np.array(U)
x = U
y = I

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5)

coefs, pcov = curve_fit(func, x[:3], y[:3])
plt.plot(x, func(x, coefs[0], coefs[1]), 'g-', label=f'Ток насыщения, {round(func(0, coefs[0], coefs[1]), 2)} мкА')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
i = func(0, coefs[0], coefs[1])
print('Ток насыщения', i)
plt.plot([0, 9], [i, i], '-', color='purple', label='$\Delta U$ = 9 В')

I = []
U = []

with open('data4.txt', 'r') as file:
    for line in file:
        U.append(float(line.split()[0]))
        I.append(float(line.split()[1]))

I = np.array(I) - I[0]
U = np.array(U)
x = U
y = I

plt.plot(x, y, 'k8', ms=5)

coefs, pcov = curve_fit(func, x[-3:], y[-3:])
plt.plot(x, func(x, coefs[0], coefs[1]), 'b-', label=f'Ток насыщения, {round(func(0, coefs[0], coefs[1]), 2)} мкА')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
i = func(0, coefs[0], coefs[1])
print('Ток насыщения', i)
plt.plot([-9.2, 0], [i, i], '-', color='cyan', label='$\Delta U$ = 9.2 В')


x = np.linspace(-20, 20)
plt.plot(x, 8 * x, 'r-', label=r'$\frac{dI}{dU} |_{U=0}$ = 8 мкА/В')


plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image3.jpg')

####################################################

I = []
U = []

with open('data5.txt', 'r') as file:
    for line in file:
        U.append(float(line.split()[0]))
        I.append(float(line.split()[1]))

I = np.array(I) - I[-1]
U = np.array(U)
x = U
y = I

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5)

coefs, pcov = curve_fit(func, x[:3], y[:3])
plt.plot(x, func(x, coefs[0], coefs[1]), 'g-', label=f'Ток насыщения, {round(func(0, coefs[0], coefs[1]), 2)} мкА')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
i = func(0, coefs[0], coefs[1])
print('Ток насыщения', i)
plt.plot([0, 7], [i, i], '-', color='purple', label='$\Delta U$ = 7 В')

I = []
U = []

with open('data6.txt', 'r') as file:
    for line in file:
        U.append(float(line.split()[0]))
        I.append(float(line.split()[1]))

I = np.array(I) - I[0]
U = np.array(U)
x = U
y = I

plt.plot(x, y, 'k8', ms=5)

coefs, pcov = curve_fit(func, x[-3:], y[-3:])
plt.plot(x, func(x, coefs[0], coefs[1]), 'b-', label=f'Ток насыщения, {round(func(0, coefs[0], coefs[1]), 2)} мкА')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
i = func(0, coefs[0], coefs[1])
print('Ток насыщения', i)
plt.plot([-7.5, 0], [i, i], '-', color='cyan', label='$\Delta U$ = 7.5 В')

x = np.linspace(-20, 20)
plt.plot(x, 6.5 * x, 'r-', label=r'$\frac{dI}{dU} |_{U=0}$ = 6.5 мкА/В')

plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image4.jpg')

####################################################

I = []
U = []

with open('data7.txt', 'r') as file:
    for line in file:
        U.append(float(line.split()[0]))
        I.append(float(line.split()[1]))

I = np.array(I) - I[-1]
U = np.array(U)
x = U
y = I

plt.figure(dpi=100)
plt.plot(x, y, 'k8', ms=5)

coefs, pcov = curve_fit(func, x[:3], y[:3])
plt.plot(x, func(x, coefs[0], coefs[1]), 'g-', label=f'Ток насыщения, {round(func(0, coefs[0], coefs[1]), 2)} мкА')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
i = func(0, coefs[0], coefs[1])
print('Ток насыщения', i)
plt.plot([0, 7.4], [i, i], '-', color='purple', label='$\Delta U$ = 7.4 В')

I = []
U = []

with open('data8.txt', 'r') as file:
    for line in file:
        U.append(float(line.split()[0]))
        I.append(float(line.split()[1]))

I = np.array(I) - I[0]
U = np.array(U)
x = U
y = I

plt.plot(x, y, 'k8', ms=5)

coefs, pcov = curve_fit(func, x[-3:], y[-3:])
plt.plot(x, func(x, coefs[0], coefs[1]), 'b-', label=f'Ток насыщения, {round(func(0, coefs[0], coefs[1]), 2)} мкА')
coef_error = np.sqrt(np.diag(pcov))
print(coefs, coef_error)
i = func(0, coefs[0], coefs[1])
print('Ток насыщения', i)
plt.plot([-7, 0], [i, i], '-', color='cyan', label='$\Delta U$ = 7 В')


x = np.linspace(-20, 20)
plt.plot(x, 3 * x, 'r-', label=r'$\frac{dI}{dU} |_{U=0}$ = 3 мкА/В')

plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image5.jpg')
