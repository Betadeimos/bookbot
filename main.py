from stats import count_words

def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
    return file_contents

def main():
    full_book = get_book_text("books/frankenstein.txt")
    num_words = count_words(full_book)
    print(f"{num_words} words found in the document")

main()