number = input()
while len(number) != 1:
    summa = 0
    for x in number:
        summa += int(x)
    number = str(summa)
print(number)
