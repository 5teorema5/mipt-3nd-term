from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

n, fi = [], []
with open("data.txt") as file:
    for f in file:
        n.append(float(f.split()[0]) / np.pi)
        fi.append(float(f.split()[1]))

n, fi = np.array(n), np.array(fi)


def func(x, a, b):
    return a * x ** 10 + b


x = n / n[13]
y = fi - 2
# y_1 = 2 * np.pi/2 - y - 0.7

coefficients = np.polyfit(x, y, 4)
fx = np.linspace(x[0], x[-1])
fy = np.polyval(coefficients, fx)

# coefficients = np.polyfit(x, y_1, 4)
# fy_1 = np.polyval(coefficients, fx)


t = max(y) / (2 ** 0.5)
print(t)

plt.figure(dpi=150)
plt.plot(x, y, 'k8', ms=3)
# plt.plot(x, y_1, 'k8', ms=3)
plt.plot(fx, fy, 'r-', label='approx by polyfit')
# plt.plot(fx, fy_1, 'r--')

plt.plot([x[0], x[-1]], [-1/4, -1/4], 'g-', label="-pi/4")
plt.plot([x[0], x[-1]], [1/4, 1/4], 'y-', label="pi/4")

# plt.plot([1.041, 1.041], [0.5, 2.5], '--', label='1.041')
# plt.plot([0.965, 0.965], [0.5, 2.5], '--', label='0.965')

print(1.041 - 0.965)

plt.xlabel('$n/n_{res}$')
plt.ylabel('$fi$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
plt.savefig('image1.png')
