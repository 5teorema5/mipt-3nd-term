from pprint import pprint
import matplotlib.pyplot as plt

colors = ['lightcyan', 'paleturquoise', 'powderblue', 'mediumturquoise', 'turquoise', 'lightseagreen', 'darkcyan',
          'teal']

students = open('doc/students.csv').readlines()
preps, groups = dict(), dict()

for s in students:
    prep, group, grade = s.split(';')

    if prep not in preps.keys():
        preps[prep] = [int(grade)]
    else:
        preps[prep].append(int(grade))

    if group not in groups.keys():
        groups[group] = [int(grade)]
    else:
        groups[group].append(int(grade))

grades_prep = dict()
all_grades = [j for j in range(3, 11)]
for prep in preps.keys():
    grades = set(preps[prep])
    for g in grades:
        if g not in grades_prep.keys():
            grades_prep[g] = [preps[prep].count(g)]
        else:
            grades_prep[g].append(preps[prep].count(g))

    for g in all_grades:
        if g not in grades:
            if g not in grades_prep.keys():
                grades_prep[g] = [0]
            else:
                grades_prep[g].append(0)

fig1 = plt.figure(figsize=(8, 6))
ax = plt.axes(xlim=(-1, 7), ylim=(0, 20))
bar_numbers = range(7)
bottom = [0] * 7
k = 0

for grade in range(3, 11):
    data = {'prep1': grades_prep[grade][0],
            'prep2': grades_prep[grade][1],
            'prep3': grades_prep[grade][2],
            'prep4': grades_prep[grade][3],
            'prep5': grades_prep[grade][4],
            'prep6': grades_prep[grade][5],
            'prep7': grades_prep[grade][6],
            }

    x = range(len(data))
    labels = list(data.keys())
    values = list(data.values())

    ax.bar(x, values, label=f"{grade}", bottom=bottom, color=colors[k])
    for j in range(len(data.keys())):
        bottom[j] += values[j]

    ax.set_xticks(bar_numbers)
    ax.set_xticklabels(labels)
    k += 1

plt.title('Marks per prep')
plt.yticks([0, 3, 6, 9, 12, 15, 18])
plt.legend()
plt.savefig('doc/MarksPerPrep.png')

new_groups = {}

for x in groups.keys():
    tmp_arr = [0] * 8
    for y in groups[x]:
        tmp_arr[y - 3] += 1
    new_groups[x] = tmp_arr

fig2 = plt.figure(figsize=(8, 6))
ax = plt.axes(xlim=(-1, 7), ylim=(0, 20))
bar_numbers = range(6)
bottom = [0] * 6
k = 0

for grade in range(3, 11):
    data = {'751': new_groups['751'][k],
            '752': new_groups['752'][k],
            '753': new_groups['753'][k],
            '754': new_groups['754'][k],
            '755': new_groups['755'][k],
            '756': new_groups['756'][k],
            }

    x = range(len(data))
    labels = list(data.keys())
    values = list(data.values())

    ax.bar(x, values, label=f"{grade}", bottom=bottom, color=colors[k])
    for j in range(len(data.keys())):
        bottom[j] += values[j]

    ax.set_xticks(bar_numbers)
    ax.set_xticklabels(labels)
    k += 1

plt.title('Marks per group')
plt.yticks([0, 3, 6, 9, 12, 15, 18])
plt.legend()
plt.savefig('doc/MarksPerGrep.png')
