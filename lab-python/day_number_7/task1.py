import matplotlib.pyplot as plt

colors = ['red', 'orange', 'green', 'cyan', 'purple']
markers = ['4', '*', '^', '.', '3']

for i in range(5):
    point_x = []
    point_y = []

    with open(f'doc/00{i+1}.dat') as file:
        n = int(file.readline().split()[0])
        for j in range(n):
            line = file.readline().split()
            point_x.append(float(line[0]))
            point_y.append(float(line[1]))

    fig, axs = plt.subplots(nrows=1, ncols=1)
    axs.scatter(point_x, point_y, color=colors[i], marker=markers[i])
    axs.grid(which='minor', linewidth=0.3, linestyle='--')
    axs.minorticks_on()
    axs.set_title(f'Number of points: {len(point_x)}')
    axs.grid()
    axs.set_aspect('equal')
    plt.savefig(f'doc/dead_moroz{i+1}.png')
