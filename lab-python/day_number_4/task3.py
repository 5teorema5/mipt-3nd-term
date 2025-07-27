num = input()
try:
    len_last_double = len(num.split('.')[1])
    new_num = float(num) - 10 ** (-1 * len_last_double)
    print(f'{new_num:.{len_last_double}f}')
except:
    print(int(num) - 1)
