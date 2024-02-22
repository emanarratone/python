def calculate_anagrams(word):
    anagrams = set()
    recursive_anagrams("", word, anagrams)
    return anagrams


def recursive_anagrams(partial, characters, anagrams):
    if len(characters) == 0:
        anagrams.add(partial)
    else:
        for index, ch in enumerate(characters):
            partial += ch
            new_characters = characters[:index] + characters[index + 1:]
            recursive_anagrams(partial, new_characters, anagrams)
            partial = partial[0:len(partial) - 1]


print(calculate_anagrams("dog"))
