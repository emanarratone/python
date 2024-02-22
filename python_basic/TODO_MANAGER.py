to_do = []

try:
    with open("todo.txt", "r") as file:
        for line in file:
            to_do.append(line.rstrip())
        file.close()
except FileNotFoundError:
    print("File inesistente o errore in apertura")


def insert():

    ins = input("Insert the new task:")
    to_do.append(ins.rstrip())


def remove():
    old_len = len(to_do)
    new_len = 0
    rmv = input("Task to remove:")
    for task in to_do:
        if task == rmv:
            to_do.remove(rmv)
            new_len = len(to_do)
    if old_len == new_len:
        print("Task not in list or wrong input.")


def show_all():
    for task in to_do:
        print(task)


def remove_type():
    old_len = len(to_do)
    new_len = 0
    rmv = input("What kind of task you want to remove?")
    for task in to_do:
        if rmv in task:
            to_do.remove(task)
    if old_len == new_len:
        print("Task not in list or wrong input.")


def close():
    try:
        with open("todo.txt", "w") as file1:
            for task in to_do:
                file1.write(task + '\n')
    except FileNotFoundError:
        print("File inesistente o errore in apertura")


while True:
    print("""
        1.insert a new task
        2.remove a task
        3.show all tasks
        4.remove task type
        5.close the program
    """)
    scelta = int(input("Action-->"))
    match scelta:
        case 1:
            insert()
        case 2:
            remove()
        case 3:
            show_all()
        case 4:
            remove_type()
        case 5:
            close()
