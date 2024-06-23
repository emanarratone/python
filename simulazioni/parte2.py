def fn1(stringa):
    min_val = 1000
    for lit in stringa:
        if lit.isdigit():
            min_val = min(int(lit), min_val)
    return min_val


res = fn1('324rrg5b')
print(res)


def check_primo(x):
    for v in range(2, x):
        if x % v == 0:
            return False
    return True


def primi(x, y):
    for val in range(x, y):
        if check_primo(val):
            yield val


res = primi(50, 60)
for el in res:
    print(el)


def check(lista, n, pos, current, best):
    if current is None:
        current = []
    if best is None:
        best = []
    if sum(current) == n:
        if not best and len(best) < len(current):
            best[:] = current[:]
            return
    if pos >= len(lista) or sum(current) > n:
        return
    check(lista[1:], n, pos+1, current+[lista[pos]], best)
    check(lista[1:], n, pos+1, current, best)
    return best


lista_partenza = [5, 6, 7, 2, 13, 11, 8, 1, 2, 1]
target = 9
res = check(lista_partenza, target, 0, None, None)
print(res)
