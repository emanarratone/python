list1 = ['pippo', 'pluto', 'paperino']
list2 = ['pip', 'paperino&paperina', 'topolino', 'minnie', 'pippo']
list3 = [(x, y) for x in list1 for y in list2 if x == y or x in y or y in x]
print(list3)
