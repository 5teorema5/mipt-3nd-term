import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

data = []
with open('doc/data.dat') as file:
    for line in file:
        data.append(float(line.split()[0]))
u0 = np.array(data)

A = np.diag(np.full(u0.shape, 1))
A[1:, :A.shape[0] - 1] += np.diag(np.full(u0.shape[0] - 1, -1))
A[0][A.shape[0] - 1] = -1

u = [u0]
for i in range(255):
    u.append(u[i] - 0.5 * np.dot(A, u[i]))
u = np.array(u)

fig = plt.figure()
axis = plt.axes(xlim=(0, 50), ylim=(0, 10))
line, = axis.plot([], [], lw=3, color='orange')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.title('Function')


def animate(i):
    line.set_data(np.arange(0, 50), [float(x) for x in u[i]])
    return line,


anim = animation.FuncAnimation(fig, animate, frames=255, interval=100, blit=True)
plt.show()
anim.save('doc/animation.gif', writer='pillow')
