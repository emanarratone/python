def ennesimo_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ennesimo_fibonacci(n-1) + ennesimo_fibonacci(n-2)


print(ennesimo_fibonacci(10))
