st = input().split()
try:
    if st[1] == '+':
        print(int(st[0]) + int(st[2]))
    elif st[1] == '-':
        print(int(st[0]) - int(st[2]))
    elif st[1] == '*':
        print(int(st[0]) * int(st[2]))
    elif st[1] == '/':
        print(int(st[0]) / int(st[2]))
    elif st[1] == '^':
        print(int(st[0]) ** int(st[2]))
    else:
        print('Bad input')
except:
    print('Bad input')
