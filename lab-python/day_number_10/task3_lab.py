import matplotlib.pyplot as plt
import numpy as np
import scipy
from sympy import symbols, Function, Eq, dsolve, plot

x = symbols('x')
y = Function('y')
dif_equation = Eq(y(x).diff(x), -2 * y(x))
solution = dsolve(dif_equation, ics={y(0): 2 ** 0.5})
print(solution.rhs)

fig1 = plot(solution.rhs, (x, 0, 10), title='Символьное решение sympy', ylabel='y', xlabel='x', show=False)
fig1[0].line_color = 'red'
fig1.save('doc/solution_1_1.png')

fig1, ax = plt.subplots(1)
x1 = np.linspace(0, 10)
y1 = []
for i in x1:
    y1.append(solution.rhs.subs(x, i))
y1 = np.array(y1)
plt.plot(x1, y1, 'r')
plt.title('Символьное решение sympy')
plt.xlabel('x')
plt.ylabel('y')

ax.set_xlim(xmin=0, xmax=10)
ax.set_ylim(ymin=0)
for pos in ['right', 'top']:
    ax.spines[pos].set_visible(False)

fig1.savefig('doc/solution_1_2.png')


def dydx(x, y):
    return -2 * y


fig2, ax = plt.subplots(1)

y0 = [np.sqrt(2)]
solution = scipy.integrate.solve_ivp(dydx, (0.0, 10), y0=y0, t_eval=np.linspace(0.0, 10, 101))

plt.plot(solution.t, solution.y[0, :], '-')
plt.title('Численное решение scipy')
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlim(xmin=0, xmax=10)
ax.set_ylim(ymin=0)
for pos in ['right', 'top']:
    ax.spines[pos].set_visible(False)
plt.savefig('doc/solution_2_1.png')


def dydx(y, x):
    return -2 * y


x = np.linspace(0, 10)
y0 = 2 ** 0.5
y2 = scipy.integrate.odeint(dydx, y0, x).flatten()

fig2, ax = plt.subplots(1)
plt.plot(x, y2)
plt.title('Численное решение scipy')
plt.xlabel('x')
plt.ylabel('y')

ax.set_xlim(xmin=0, xmax=10)
ax.set_ylim(ymin=0)
for pos in ['right', 'top']:
    ax.spines[pos].set_visible(False)

fig2.savefig('doc/solution_2_2.png')

fig3, ax = plt.subplots(1)
plt.plot(x, y2 - y1, '-.g')
plt.title('Разница решений решений sympy и scipy')
plt.xlabel('x')
plt.ylabel('y')

for pos in ['right', 'top']:
    ax.spines[pos].set_visible(False)

fig3.savefig('doc/solution_3.png')
