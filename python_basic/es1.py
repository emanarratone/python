string1 = input("inserire una stringa: ")
string2 = input('inserire un altra stringa: ')

string11 = ''
string22 = ''

if not string1 or not string2:
    print("Errore, una delle stringhe o entrambe sono vuote")
else:
    string11 = str(string1[0] + string2[1:])
    string22 = str(string2[0] + string1[1:])
print("swapped 1: "+string11)
print("swapped 2: "+string22)


