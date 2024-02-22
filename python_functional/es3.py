lista = ['uno', 'due', 'tre', 'quattro']
list1 = []


def f1():
    for word in lista:
        list1.append(len(word))


def f2(n):
    return len(n)


list2 = list(map(f2, lista))
f1()
print(list1)
print('-------------------')
print(list2)
list3 = [len(el) for el in lista]
print('-------------------')
print(list3)
