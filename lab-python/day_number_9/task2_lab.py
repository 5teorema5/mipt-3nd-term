import matplotlib.pyplot as plt
import numpy as np

paths = ['signal01.dat', 'signal02.dat', 'signal03.dat']

for path in paths:
    data = []
    with open('doc/' + path) as file:
        for line in file:
            data.append(float(line.split()[0]))

    data = np.array(data)

    data_filter = []
    for i in range(len(data)):
        if i < 10:
            d = [data[j] for j in range(i + 1)]
        else:
            d = [data[j] for j in range(i - 9, i + 1)]
        data_filter.append(sum(d) / len(d))

    N = 10
    mean_kernel = np.ones(N) / N
    data_filter_np = np.convolve(data, mean_kernel, mode='same')

    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))

    axs[0].plot(data)
    axs[0].set_title('До обработки')
    axs[0].grid()
    axs[0].set_ylim(0, data.max())
    axs[1].plot(data_filter)
    axs[1].set_title('После обработки')
    axs[1].grid()
    axs[1].set_ylim(0, data.max())
    axs[2].plot(data_filter_np)
    axs[2].set_title('После обработки np')
    axs[2].grid()
    axs[2].set_ylim(0, data.max())
    fig.savefig('doc/update_' + path[:path.index('.')+1] + 'png')

