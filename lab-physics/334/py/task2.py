from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def func(x, k, b):
    return k * x + b

I, V0, Im, V = [], [], [], []
B = []
K = []

with open('data2.txt') as file:
    for i in range(7):
        I.append(float(file.readline().split()[0]))
        V0.append(float(file.readline().split()[0]))
        for j in range(18):
            tmp = file.readline().split()
            Im.append(float(tmp[0]))
            V.append(float(tmp[1]))

with open('data.txt') as file:
    for f in file:
        B.append(round(float(f.split()[2]), 3))

Im1, Im2, Im3, Im4, Im5, Im6, Im7 = np.array(Im[:18]), np.array(Im[18:36]), np.array(Im[36:54]), np.array(
    Im[54:72]), np.array(Im[72:90]), np.array(Im[90:108]), np.array(Im[108:])
V1, V2, V3, V4, V5, V6, V7 = (np.array(V[:18]) - V0[0], np.array(V[18:36]) - V0[1], np.array(V[36:54]) - V0[2],
                              np.array(V[54:72]) - V0[3], np.array(V[72:90]) - V0[4], np.array(V[90:108]) - V0[5],
                              V0[6] - np.array(V[108:]))

B = np.array([0.00746667, 0.01333333, 0.01866667, 0.02466667, 0.03066667, 0.03773333,
              0.04266667, 0.0484, 0.054, 0.0588, 0.06453333, 0.06933333,
              0.0732, 0.07733333, 0.08, 0.08253333, 0.08533333, 0.08666667]) * 10 ** 4

plt.figure(dpi=200)

coefs, pcov = curve_fit(func, B, V1)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V1, color='red', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='red', marker='', linestyle='-', label='$I_{m}$ = 0.3 mA')

print('------------------------------')

coefs, pcov = curve_fit(func, B, V2)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V2, color='orange', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='orange', marker='', linestyle='-', label='$I_{m}$ = 0.4 mA')

print('------------------------------')

coefs, pcov = curve_fit(func, B, V3)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V3, color='yellow', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='yellow', marker='', linestyle='-', label='$I_{m}$ = 0.5 mA')

print('------------------------------')

coefs, pcov = curve_fit(func, B, V4)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V4, color='green', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='green', marker='', linestyle='-', label='$I_{m}$ = 0.6 mA')

print('------------------------------')

coefs, pcov = curve_fit(func, B, V5)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V5, color='cyan', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='cyan', marker='', linestyle='-', label='$I_{m}$ = 0.7 mA')

print('------------------------------')

coefs, pcov = curve_fit(func, B, V6)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V6, color='blue', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='blue', marker='', linestyle='-', label='$I_{m}$ = 0.8 mA')

print('------------------------------')

coefs, pcov = curve_fit(func, B, V7)
coef_error = np.sqrt(np.diag(pcov))
print(coefs)
K.append(coefs[0])
print(coef_error)
plt.plot(B, V7, color='purple', marker='.', linestyle='')
plt.plot(B, func(B, coefs[0], coefs[1]), color='purple', marker='', linestyle='-', label='$I_{m}^{flip}$ = 0.85 mA')

print('------------------------------')

plt.xlabel('B, мТл')
plt.ylabel('$\mathcal{E}_x$, мВ')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image2.jpg')

print(K)
