from stats import count_words, get_book_text, count_characters



def main():
    full_book = get_book_text("books/frankenstein.txt")
    num_words = count_words(full_book)
    print(f"{num_words} words found in the document")

main()