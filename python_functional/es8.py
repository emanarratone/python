def med(lis):
    n = 1
    sm = 0
    for num in lis:
        sm = (sm * (n-1) + num)/n
        n += 1
        print(f"sent: {num}, new average: {sm}")
        yield sm


list1 = [7, 13, 17, 231, 12, 8, 3]

media = med(list1)

for els in list1:
    next(media)
