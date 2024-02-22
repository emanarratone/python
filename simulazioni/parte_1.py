def test_ifs(a, b, c):
    if a or b:
        if b:
            print('1')
        else:
            print('2')
    if a and c:
        print('3')
    elif b and c:
        print('4')
    else:
        print('5')
    if c:
        print('6')
    else:
        print('7')


test_ifs(0, 0, 0)   #stampa 5 7
test_ifs([0], 0, [0])   # stampa 2 3 6
test_ifs({}, (3, 4), -1)    # stampa 1 3 6 (le collezioni vuote sono false)
test_ifs(False, (), {0})    # stampa 5 6 (daje)
test_ifs(max(1, 0), min(1, 0), -1)  # stampa 2 3 6
test_ifs([()], 4, 1-1)  # stampa 1 5 7


def fn1(a):
    a.extend(range(5, 7))
    fn2(a)


def fn2(b):
    b = [3, 4, 5]
    b.append(8)


my_list = [1, 2, 3, 4]
fn1(my_list)
print(my_list)
    # stampa 1 2 3 4 5 6 (le chiamate su fn2 non modificano la lista)

x = list(range(-10, 30, 5))
print(x[1:])    # stampa da -5 a 25
print(x[:1])    # stampa -10 (:1 indica che si fermerà all'elemento 1)
print(x[1])     # stampa -5
print(x[2:4])   # stampa 0 5 (start incluso, end escluso)
print(x[-4:-2])  # stampa 5 10 (da sinistra si inizia da 1 non 0)
print(x[-2::-2])    # stampa dal secondo elemento da destra verso sinistra
                    # ([-2:]) e alternando ogni due ([::-2])

print([x+y for x in [2, 5] for y in [1, 5] if x != y])    # stampa 3
print([x[1] % x[0] for x in [(5, 10), (4, 25), (3, 7)]])  # stampa 0 1 1
print([min(x) for x in zip('fbb', 'pra', 'ola', 'qbc')])   # stampa FBA
print(next(x*2 for x in range(5, 10)))  # stampa 10 (generatore quindi solo uno, il primo)
print(min([('bici', 2), ('auto', 4), ('moto', 2)], key=lambda x: x[1]))  # stampa bici
