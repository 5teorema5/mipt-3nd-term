import pandas as pd

matrix = pd.read_csv('data.csv')
matrix.index = matrix.columns

print(matrix)

arr, new_arr = [], []

for x in matrix.columns.to_list():
    tmp = matrix.loc[:, x]
    for y in tmp[tmp>0].index.to_list():
        if x <= y:
            arr.append([x, y, matrix.loc[x, y]])

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

for x in arr:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
    if x[1] not in group[x[0]]:  # если вершины принадлежат разным группам, то объединяем
        arr_ribs.append(x)
        gr1 = group[x[0]]
        group[x[0]] += group[x[1]]  # объединяем списки двух групп вершин
        group[x[1]] += gr1

print(arr_ribs)