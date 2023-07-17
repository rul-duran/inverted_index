def inverted_index_to_text(inverted_index={}):
    words_list = []
    text = ''
    for word, indices in inverted_index.items():
        for index in indices:
            words_list.insert(index, f' {word}')
    return text.join(words_list)
