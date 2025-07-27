from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k, b):
    return k * x + b


dict = {}
with open('data.txt', 'r') as file:
    for line in file:
        w = round(abs(float(line.split()[2]) - float(line.split()[1])), 3)
        dict[line.split()[0]] = round(w/0.0072 / 1000, 3)

fig, ax = plt.subplots(dpi=80, figsize=(10, 6))

color_arr = ['red', 'red', 'purple', 'purple', 'green', 'green', 'blue', 'blue']
line_arr = ['-', '-.', '-', '-.', '-', '-.', '-', '-.']
d = np.array([1, 1, 1, 1, 0.86, 0.86, 1, 1]) / 100
s = np.pi * d ** 2 / 4
sigma_s = s * 2 * 0.0001 / d
mu_0 = 4 * np.pi * 10 ** (-7)

for i in range(1, 9):
    P, B = [], []
    with open(f'data2_{i}.txt', 'r') as file:
        tmp = file.readline().split()
        name = str(tmp[0]) + ' ' + str(tmp[1])
        for line in file:
            P.append(float(line.split()[1]) / 10 ** 6 * 10)
            B.append(dict[line.split()[0]])

    P = np.array(P)
    B = np.array(B)

    x = B**2
    y = P

    coefs, pcov = curve_fit(func, x, y)

    plt.plot(x, y, 'k8', ms=5, label=name)

    plt.plot(x, func(x, coefs[0], coefs[1]), color=color_arr[i-1], linestyle=line_arr[i-1], label=f'k = {round(coefs[0] * 1000, 3)} мН/Тл^2')

    coef_error = np.sqrt(np.diag(pcov))

    # print(coefs, coef_error)

    chi = 2 * coefs[0] * mu_0 / s[i-1]
    sigma_chi = chi * np.sqrt((coef_error[0]/coefs[0])**2 + (sigma_s[i-1]/s[i-1])**2)
    print(rf'{line_arr[i-1]} & {round(coefs[0] * 10**4, 3)} & {round(coef_error[0] * 10**4, 3)} & {round(coef_error[0]/coefs[0]*100, 1)} & {round(chi * 10**6, 3)} & {round(sigma_chi * 10**6, 3)} & {round(sigma_chi / chi * 100, 1)} \\ \hline')

sf = plt.ScalarFormatter()
sf.set_powerlimits((-4, 4))
ax.yaxis.set_major_formatter(sf)

plt.ylabel(r'$P, Н$')
plt.xlabel(r'$B^2, Тл^2$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
plt.savefig(f'image2.jpg')