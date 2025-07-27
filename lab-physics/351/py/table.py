i = 1
with open('data7.txt', 'r') as file:
    for line in file:
        # tmp = round(float(line.split()[3]) / float(line.split()[4]), 2)
        # print(f'{i} & {line.split()[0]} & {line.split()[1]} & {line.split()[2]} & {tmp} \hline')
        print(rf'{i} & {line.split()[0]} & {line.split()[1]} \\ \hline')

        i += 1

with open('data8.txt', 'r') as file:
    for line in file:
        # tmp = round(float(line.split()[3]) / float(line.split()[4]), 2)
        # print(f'{i} & {line.split()[0]} & {line.split()[1]} & {line.split()[2]} & {tmp} \hline')
        print(rf'{i} & {line.split()[0]} & {line.split()[1]} \\ \hline')

        i += 1
