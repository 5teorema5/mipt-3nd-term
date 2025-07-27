def ROT13(a):
    if x.isalpha():
        if a.islower():
            if ord(a) + 13 > ord('z'):
                return str(chr(ord(a) - 13))
            return str(chr(ord(a) + 13))
        if ord(a) + 13 > ord('Z'):
            return str(chr(ord(a) - 13))
        return str(chr(ord(a) + 13))
    return a


try:
    path, text, text_ = input(), '', ''
    with open(path, 'r') as file:
        for x in file:
            for y in x:
                text += ROT13(ROT13(y))

    print(text)

    for x in text:
        for y in x:
            text_ += ROT13(y)

    print(text_)
except:
    print('Can not read file')
