stringa = input("inserire una stringa")
dic = stringa.split()
freq = {}
for el in dic:
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

print(freq)
