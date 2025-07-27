i = 1
with open('data.txt', 'r') as file:
    for line in file:
        print(rf'{i} & {line.split()[0]} & {float(line.split()[1])} \\ \hline')

        i += 1
