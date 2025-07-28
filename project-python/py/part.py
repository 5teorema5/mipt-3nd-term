import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

fig1 = plt.figure()
graph = nx.Graph()

data = pd.read_csv('data.csv')
data.index = data.columns

total_weight = 0
for i in range(data.shape[0]):
    for j in range(i, data.shape[1]):
        total_weight += data.iloc[i, j]
        if data.iloc[i, j] != 0:
            graph.add_edge(f'{data.columns[i]}', f'{data.columns[j]}', weight=data.iloc[i, j])

pos = nx.planar_layout(graph)
# nx.circular_layout
# nx.draw_kamada_kawai
# nx.draw_planar
# nx.draw_random
# nx.draw_spectral
# nx.draw_spring
# nx.draw_shell
nx.draw_networkx_nodes(graph, pos, node_size=300, node_color='yellow')
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels)
nx.draw_networkx_edges(graph, pos, width=2, edge_color='black')
nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels)

print(total_weight)

plt.axis("off")
plt.title(rf'План решения проблемы поставки виски (было {total_weight})')
plt.savefig("image_3_1.png")

fig2 = plt.figure()

arr, new_arr = [], []

for x in data.columns.to_list():
    tmp = data.loc[:, x]
    for y in tmp[tmp > 0].index.to_list():
        if x <= y:
            arr.append([x, y, data.loc[x, y]])

arr.sort(key=lambda x: x[2], reverse=False)

arr_ver_connected = set()  # список соединенных вершин
group = {}  # словарь списка изолированных групп вершин
arr_ribs = []  # список ребер остова

for x in arr:
    if x[0] not in arr_ver_connected or x[1] not in arr_ver_connected:  # проверка для исключения циклов в остове
        if x[0] not in arr_ver_connected and x[1] not in arr_ver_connected:  # обе вершины не соединены
            group[x[0]] = [x[0], x[1]]  # формируем в словаре ключ с номерами вершин
            group[x[1]] = group[x[0]]  # и связываем их с одним и тем же списком вершин
        else:
            if not group.get(x[0]):  # в словаре нет первой вершины
                group[x[1]].append(x[0])  # добавляем в список первую вершину
                group[x[0]] = group[x[1]]  # добавляем ключ с номером первой вершины
            else:
                group[x[0]].append(x[1])  # то же самое делаем со второй вершиной
                group[x[1]] = group[x[0]]

        arr_ribs.append(x)
        arr_ver_connected.add(x[0])
        arr_ver_connected.add(x[1])
    else:
        if x[1] not in group[x[0]]:  # если вершины принадлежат разным группам, то объединяем
            arr_ribs.append(x)
            gr1 = group[x[0]]
            group[x[0]] += group[x[1]]  # объединяем списки двух групп вершин
            group[x[1]] += gr1

new_arr = arr_ribs

new_graph = nx.Graph()

total_weight = 0
for x in new_arr:
    new_graph.add_edge(f'{x[0]}', f'{x[1]}', weight=x[2])
    total_weight += x[2]

nx.draw_networkx_nodes(new_graph, pos, node_size=300, node_color='yellow')
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels)
nx.draw_networkx_edges(graph, pos, width=2, edge_color='red')
nx.draw_networkx_edges(new_graph, pos, width=2, edge_color='green')
nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels)

print(total_weight)

plt.axis("off")
plt.title(rf'План решения проблемы поставки виски (стало {total_weight})')
plt.savefig("image_3_2.png")
