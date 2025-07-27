import pandas as pd
import matplotlib.pyplot as plt

# merge data

students = pd.read_excel("doc/students_info.xlsx")
students.columns = ['User', 'group_faculty', 'group_out']
students = students.dropna().sort_values('User')
results = pd.read_html("doc/results_ejudge.html")[0]
data = pd.merge(results, students, on='User').sort_values('group_faculty')

# task 1

group_faculty = dict()
group_inf = dict()

group_arr = ['group_faculty', 'group_out']

for j, obj in enumerate([group_faculty, group_inf]):
    for i in range(students[group_arr[j]].min(), students[group_arr[j]].max() + 1):
        tmp_data = data.loc[data[group_arr[j]] == i].sum()
        if data[data[group_arr[j]] == i].loc[:, 'User'].size != 0:
            obj[i] = tmp_data['Solved'] / data[data[group_arr[j]] == i].loc[:, 'User'].size
        else:
            obj[i] = 0

# graph

fig, axs = plt.subplots(nrows=1, ncols=2)

title_array = ['group_faculty', 'group_inf']
xlabel_array = ['Номер факультетской группы', 'Номер группы по информатике']

for k, obj in enumerate([group_faculty, group_inf]):

    labels = list(obj.keys())
    values = list(obj.values())
    axs[k].bar(labels, values)
    axs[k].set_title(title_array[k])
    for i in range(len(group_faculty.keys())):
        axs[k].text(labels[i], values[i], round(values[i], 2), ha='center')
    axs[k].grid()
    axs[k].set_xlabel(xlabel_array[k])
    axs[k].set_ylabel('Среднее количество решённых задач')
    axs[k].set_xticks(labels, labels=labels)

plt.savefig('doc/results_ejudge.png')

# task 2

data2 = data[(data['G'] > 10) | (data['H'] > 10)].reset_index().loc[:, ['group_faculty', 'group_out']]
print(data2)
