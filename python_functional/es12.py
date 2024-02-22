task1 = {'todo': 'call John for project organization', 'deadline': (27, 5, 2022), 'urgent': True}
task2 = {'todo': 'buy a new mouse', 'deadline': (27, 12, 2021), 'urgent': True}
task3 = {'todo': 'find a present for Angelina’s birthday', 'deadline': (3, 2, 2022), 'urgent': False}
task4 = {'todo': 'organize mega party (last week of April)', 'deadline': (27, 11, 2021), 'urgent': False}
task5 = {'todo': 'book summer holidays', 'deadline': (13, 6, 2022), 'urgent': False}
task6 = {'todo': 'whatsapp Mary for a coffee', 'deadline': (30, 10, 2021), 'urgent': False}
tasks = [task1, task2, task3, task4, task5, task6]


def is_urgent(task):
    return task['urgent']


def by_year(task):
    for date in task['deadline']:
        if date == 2021:
            return task


filt1 = list(filter(is_urgent, tasks))
print(filt1)
print('---------------------------')
filt2 = list(filter(by_year, tasks))
print(filt2)
print('---------------------------')
filt3 = sorted(tasks, key=lambda x: (x['deadline'][2], x['deadline'][1], x['deadline'][0]))
print(filt3)
