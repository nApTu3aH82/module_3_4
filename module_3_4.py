def single_root_words(root_words, *other_words):
    same_words = []
    for count in range(len(other_words)):
        if root_words.upper() in str(other_words[count]).upper() or str(
                other_words[count]).upper() in root_words.upper():
            same_words.append(other_words[count])
    return (same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
