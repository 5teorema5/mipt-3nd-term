
d = {}
with open('data.txt', 'r') as file:
    for line in file:
        w = round(abs(float(line.split()[2]) - float(line.split()[1])), 3)
        d[line.split()[0]] = round(w/0.0072 / 1000, 3)
with open('data2.txt', 'r') as file:
    for j in range(4):
        a = file.readline()
        print(a)
        for k in range(19):
            b = file.readline().split()
            print(rf'{b[0]} & {d[b[0]]} & {round(float(b[1]) * 9.8, 3)} \\ \hline')


    # for line in file:
        # tmp = round(float(line.split()[3]) / float(line.split()[4]), 2)
        # print(f'{i} & {line.split()[0]} & {line.split()[1]} & {line.split()[2]} & {tmp} \hline')
        # w = round(abs(float(line.split()[2])-float(line.split()[1])), 3)
        # print(rf'{line.split()[0]} & {w} & {round(w/0.0072 / 1000, 3)} \\ \hline')
        #
        # i += 1
