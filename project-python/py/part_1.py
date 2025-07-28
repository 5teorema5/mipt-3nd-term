import pandas as pd


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.index = -1

    def add_connection(self, node, weight):
        self.connections.append([node, weight])


class Matrix:
    def __init__(self, arr_nodes):
        self.size = len(arr_nodes)
        self.nodes = arr_nodes
        for i, node in enumerate(arr_nodes):
            node.index = i
        self.matrix = pd.DataFrame([[0] * self.size for _ in range(self.size)],
                                   columns=[node.name for node in arr_nodes],
                                   index=[node.name for node in arr_nodes])
        for i in range(len(arr_nodes)):
            for j in range(len(arr_nodes[i].connections)):
                self.matrix.iloc[arr_nodes[i].index, arr_nodes[i].connections[j][0].index] = \
                    arr_nodes[i].connections[j][1]
                self.matrix.iloc[arr_nodes[i].connections[j][0].index, arr_nodes[i].index] = \
                    arr_nodes[i].connections[j][1]

    def print_matrix(self):
        print(self.matrix)


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.add_connection(b, 5)
a.add_connection(c, 10)
a.add_connection(e, 20)
b.add_connection(c, 2)
b.add_connection(d, 4)
c.add_connection(d, 7)
c.add_connection(f, 10)
d.add_connection(e, 3)

G = Matrix([a, b, c, d, e, f])
G.print_matrix()

G.matrix.to_csv('data.csv', sep=',', index=False, encoding='utf-8')