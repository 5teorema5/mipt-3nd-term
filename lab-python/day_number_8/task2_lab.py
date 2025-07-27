import pandas as pd
import matplotlib.pyplot as plt

results = dict()

data = pd.read_csv('doc/flights.csv')
cargo = set(data['CARGO'].to_list())
for name in cargo:
    tmp_data = data.loc[data['CARGO'] == name]
    count = tmp_data.loc[:, 'PRICE'].size
    tmp_data = tmp_data.sum()
    results[name] = [count, tmp_data['PRICE'], tmp_data['WEIGHT']]

data_graph_1 = dict()
data_graph_2 = dict()
data_graph_3 = dict()

for x in results.keys():
    for k, obj in enumerate([data_graph_1, data_graph_2, data_graph_3]):
        obj[x] = results[x][k]
    print(f'{x}\t->\tcount = {results[x][0]}, \tall_price = {results[x][1]},\tall_weight = {results[x][2]}')

# graph

width = 0.2
bar_numbers = range(len(data_graph_1))
labels_bar = ['count', 'all price, *100', 'all weight, * 5']

fig, axs = plt.subplots(nrows=1, ncols=3)
fig.set_figwidth(12)
fig.set_figheight(5)
title_array = ['count', 'all price', 'all weight']

for k, obj in enumerate([data_graph_1, data_graph_2, data_graph_3]):
    labels = list(obj.keys())
    values = list(obj.values())
    axs[k].bar(labels, values)
    axs[k].set_title(title_array[k])
    for i in range(len(labels)):
        axs[k].text(labels[i], values[i], round(values[i], 2), ha='center')
    axs[k].grid()
    axs[k].set_xticks(labels, labels=labels)

plt.savefig('doc/flights.png')
