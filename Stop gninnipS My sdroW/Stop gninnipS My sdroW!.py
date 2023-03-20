def spin_words(sentence):
    word = list(sentence.split())
    new_word = []
    for i in word:
        if len(i) >= 5:
            new_word.append(i[::-1])
        else:
            new_word.append(i)
    return ' '.join(new_word)
