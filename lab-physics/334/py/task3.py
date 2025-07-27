from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def func(x, k):
    return k * x


SN = 75 * 10 ** (-4)  # m^2

K = np.array([0.002128459132616412, 0.002568294371507328, 0.0030569345731752406, 0.003254112819297146, 0.003575433113139597,
     0.004150900627685304, 0.007544837912963208])
I = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85]) * 10**(-3)

coefs, pcov = curve_fit(func, I[:-1], K[:-1])

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)

plt.figure(dpi=100)
plt.plot(I, K, 'k8', ms=5)

plt.plot(I[:-1], func(I[:-1], coefs[0]), 'r-', label='approx by mnk')
# plt.title('Теоретические и экспериментальные значения\nпериодов исследуемых колебаний')
plt.xlabel('$I_m$, mA')
plt.ylabel('K, В/Тл')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.savefig('image3.jpg')
