lista = [1, -100, -12, 10, 2, -3, -4, 239, 42, 556]

lis_res = [x for x in lista if x % 2 == 0 and x > 0]
print(lis_res)


def armonic_gen(n):
    tot = 0
    for x in range(1, n+1):
        tot += 1/x
        yield tot


n = armonic_gen(5)

for _ in n:
    print(_)


lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def only_divs(lista1, num, res, pos):
    if pos >= len(lista1):
        return res
    if lista1[pos] % num == 0:
        res.append(lista1[pos])
    return only_divs(lista1, num, res, pos + 1)


new_lis = only_divs(lis, 2, [], 0)
print(new_lis)
s
