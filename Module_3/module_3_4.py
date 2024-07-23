def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        word_low = word.lower()
        if word_low in root_word or root_word in word_low:
            same_words.append(word)
    return same_words

print(single_root_words('dor', 'dura', 'Dora', 'doradura', 'dororo', 'durka'))