def in_list(n, lis):
    return bin_rec(n, 0, len(lis) - 1, lis)


def bin_rec(n, left, right, lis):
    if left > right:

        print('Elemento non trovato')
        return -1
    else:
        mid = int((left + right) / 2)
        if lis[mid] == n:
            return mid
        elif lis[mid] < n:
            return bin_rec(n, mid + 1, right, lis)
        else:
            return bin_rec(n, left, mid - 1, lis)


list_or = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos = in_list(4, list_or)

print(pos)
