def filt(lis, n):
    return filter(lambda x: len(x) > n, lis)


lista = ['uno', 'due', 'tre', 'quattro', 'cinque', 'sei']
j = 4
new_lis = list(filt(lista, j))

print(new_lis)
