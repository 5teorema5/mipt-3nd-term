import matplotlib.animation as animation
import matplotlib.pyplot as plt

fig = plt.figure()
axis = plt.axes(xlim=(0, 15), ylim=(-15, 15))
line, = axis.plot([], [], lw=3, color='purple')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.title('Function')

file = open('doc/data2.txt')

def animate(i):
    line.set_data([float(x) for x in file.readline().split()], [float(x) for x in file.readline().split()])
    return line,


anim = animation.FuncAnimation(fig, animate, frames=5, interval=256, blit=True)

anim.save('doc/animation.gif', writer='pillow')
