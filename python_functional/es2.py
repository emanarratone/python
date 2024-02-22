def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fib()

for _ in range(1000):
    print(next(fib_gen))
