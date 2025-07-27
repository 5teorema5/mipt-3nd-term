from pprint import pprint

path = input()
students = dict()
count_s, count_neud = 0, 0

try:
    with open(path, 'r') as file:
        for line in file:
            name, star = line.split(';')[0], line.split(';')[1].split()[0]
            students[name] = star

    pprint(students)

    for name in students.keys():
        count_s += 1
        if students[name] == '2' or students[name] == 'Н':
            count_neud += 1

    print(int(count_neud/count_s * 100))

except:
    print('no data')