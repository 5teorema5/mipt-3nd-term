with open(input()) as file:
    print(max([a for b in [x.split() for x in file] for a in b], key=len))
