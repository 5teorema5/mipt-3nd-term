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
plt.plot(x, y, 'k8', ms=5, color='red', label='$I_р$ = 5 мА')

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

plt.plot(x, y, 'k8', ms=5, color='red')

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

plt.plot(x, y, 'k8', ms=5, color='green', label='$I_р$ = 5 мА')

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

plt.plot(x, y, 'k8', ms=5, color='green')

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

plt.plot(x, y, 'k8', ms=5, color='blue', label='$I_р$ = 1.5 мА')

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

plt.plot(x, y, 'k8', ms=5, color='blue')

plt.xlabel('U, В')
plt.ylabel('I, мкА')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image6.jpg')
