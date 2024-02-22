string = 'abcde'
tup = ([1, 1, 2, -1, 3])
res = ''
i = 0
for el in tup:
    tup_val = tup[i]
    x = ord(string[i]) + tup_val
    res += chr(x)           # += appena il carattere alla fine della stringa
    i = i + 1
print(res)
