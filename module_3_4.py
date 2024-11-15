def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        a = root_word.lower() in word.lower()
        b = word.lower() in root_word.lower()
        if a == True or b == True:
            same_words.append(word)
        else:
            continue

    return same_words


result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result_1)

result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result_2)
