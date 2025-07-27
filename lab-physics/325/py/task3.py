from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

n, u, x, fi = [], [], [], []
with open("data.txt") as file:
    for f in file:
        n.append(float(f.split()[0]))
        u.append(float(f.split()[1]))
        x.append(float(f.split()[2])*10**(-6))
        fi.append(float(f.split()[0]) * float(f.split()[2]) * 2 * 10**(-6) * np.pi)

n, u, x, fi = np.array(n), np.array(u), np.array(x), np.array(fi)


def func(x, a, b):
    return a * x ** 10 + b


x1 = n / n[8]
y1 = u / u[8]
y2 = fi
y2_1 = 2 * 1.35 - y2

# coefficients = np.polyfit(x1, y1, 7)
# fx1 = np.linspace(x1[0], x1[-1])
# fy1 = np.polyval(coefficients, fx1)
#
# t = max(y1) / (2 ** 0.5)
# print(t)
#
# plt.figure(dpi=150)
# plt.plot(x1, y1, 'k8', ms=3)
#
# plt.plot([1.0537, 1.0537], [min(y1), max(y1)], '--', label='1.0537')
# plt.plot([0.9538, 0.9538], [min(y1), max(y1)], '--', label='0.9538')
#
# print(1.0537 - 0.9538)
#
# plt.plot(fx1, fy1, 'r-', label='approx by polyfit')
# plt.plot([0.9538, 1.0537], [t, t], 'g-o')
# plt.xlabel('$n/n_{res}$')
# plt.ylabel('$U/U_{res}$')
# plt.grid(which='minor', linewidth=0.3, linestyle='--')
# plt.minorticks_on()
# plt.grid()
# plt.legend()
# plt.show()

coefficients = np.polyfit(x1, y2, 7)
fx1 = np.linspace(x1[0], x1[-1])
fy2 = np.polyval(coefficients, fx1)

coefficients = np.polyfit(x1, y2_1, 7)
fy2_1 = np.polyval(coefficients, fx1)


t = max(y2) / (2 ** 0.5)
print(t)

plt.figure(dpi=150)
plt.plot(x1, y2, 'k8', ms=3)
plt.plot(x1, y2_1, 'k8', ms=3)
plt.plot(fx1, fy2, 'r-', label='approx by polyfit')
plt.plot(fx1, fy2_1, 'r--')

plt.plot([x1[0], x1[-1]], [1.35, 1.35], 'g-', label="1.35")
plt.plot([x1[0], x1[-1]], [np.pi/4, np.pi/4], 'y-', label="pi/4")

plt.plot([1.041, 1.041], [0.5, 2.5], '--', label='1.041')
plt.plot([0.965, 0.965], [0.5, 2.5], '--', label='0.965')

print(1.041 - 0.965)

plt.xlabel('$n/n_{res}$')
plt.ylabel('$fi$')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()
plt.savefig('image.png')

# with open("data.txt") as file:
#     for f in file:
#         f = f.split()
#         print(f"{f[0]} & {f[1]} & {f[2]} & {round(float(f[0])*float(f[1])*float(f[2])*10**(-6), 3)} \ \ \hline")
