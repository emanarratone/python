def x_esp(x):
    if 'X' not in x:
        print(x)
    else:
        pos = x.find('X')
        print(x[:pos] + '0' + x[pos + 1:])
        print(x[:pos] + '1' + x[pos + 1:])
        x_esp(x[:pos] + '0' + x[pos + 1:])
        x_esp(x[:pos] + '1' + x[pos + 1:])


val1 = '01X0X'
x_esp(val1)
