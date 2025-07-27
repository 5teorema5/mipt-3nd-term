from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k):
    return k * x


SN = 75 * 10 ** (-4)  # m^2

I = []  # A
dW = []  # mWb
with open('data.txt', 'r') as file:
    for f in file:
        I.append(float(f.split(' ')[0]))
        dW.append(abs(float(f.split(' ')[1]) - float(f.split(' ')[2])))

I = np.array(I)
dW = np.array(dW)

B = dW / SN  # mTl

print([round(i, 3) for i in I])
print([round(w, 3) for w in dW])
print([round(b, 3) for b in B])

coefs, pcov = curve_fit(func, I[:-6], B[:-6])

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)

plt.figure(dpi=100)
plt.plot(I, B, 'k8', ms=5, label='Экспериментальные данные')

plt.plot(I[:-6], func(I[:-6], coefs[0]), 'r-', label='approx by mnk')
# plt.title('Теоретические и экспериментальные значения\nпериодов исследуемых колебаний')
plt.xlabel('$I_m$, A')
plt.ylabel('B, мТл')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image1.jpg')
