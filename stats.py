def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def count_words(contents):    
    split_words = contents.split()
    num_words = 0
    for words in split_words:
        num_words += 1
    return num_words

def count_characters(words):
    pass