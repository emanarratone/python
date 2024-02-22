stringa = input("Inserire una stringa: ")
if stringa == '\0':
    print('ERRORE:..stringa vuota..')
else:
    stringaz = stringa[::2]
    print(stringaz)
    