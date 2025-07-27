def number(n):
    new_number = ''
    if '+' in n:
        new_number += '8'
        for x in n[2:]:
            try:
                new_number += str(int(x))
            except:
                pass
    else:
        for x in n:
            try:
                new_number += str(int(x))
            except:
                pass
    return new_number

spam_book, phone_book, phone_number = [], [], 0
for i in range(3):
    spam_book.extend(input().split(', '))
phone_book.extend(input().split(', '))
phone_number = number(input())

spam_book = [number(x) for x in spam_book]
phone_book = [number(x) for x in phone_book]

if phone_number in phone_book:
    print('NOT SPAM')
elif spam_book.count(phone_number) >= 2:
    print('SPAM')
else:
    print('NOT SPAM')

