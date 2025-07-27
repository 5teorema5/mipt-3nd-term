path, word, st = input(), input(), ''
try:
    with open(path, 'r') as file:
        for x in file:
            if '\n' in x:
                x = x[:-1]
            st += x.lower() + ' '
    print(st.split().count(word.lower()))
except:
    print(0)
