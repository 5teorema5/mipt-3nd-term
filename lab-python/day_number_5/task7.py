s = input()
new_str = ''
up = 1
for i in range(len(s)):
    if s[i] == ' ' and len(new_str) > 0:
        if new_str[-1] != ' ' and s[i + 1] not in ' ,.!?':
            new_str += s[i]
    elif s[i] != ' ':
        if s[i] in '!?':
            up = 1
            new_str += s[i] + ' '

        else:
            if up == 1:
                new_str += s[i].upper()
                up = 0
            else:
                new_str += s[i]

print(new_str)
