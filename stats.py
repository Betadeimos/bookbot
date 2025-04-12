def count_words(contents):    
    split_words = contents.split()
    num_words = 0
    for words in split_words:
        num_words += 1
    return num_words