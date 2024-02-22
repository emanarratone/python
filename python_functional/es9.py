def read_line(lis):
    for file in lis:

        try:
            with open(file, 'r') as txt:
                for line in txt.read().splitlines():
                    next_line = (yield line)
                    if next_line:
                        txt.close()
                        break
        except StopIteration():
            print("FINE")
            txt.close()
            break


def display(lis):
    rl = read_line(lis)
    while True:
        inp = input()

        if inp == 'n':
            print(rl.send('next'))
        else:
            print(next(rl))


lis_file = ["file1.txt", "file2.txt", "file3.txt"]
display(lis_file)
