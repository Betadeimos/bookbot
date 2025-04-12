from stats import count_words, get_book_text, count_characters, sort_on
import sys

def main():
	if len(sys.argv) == 2:
		book = sys.argv[1]
		full_book = get_book_text(book)
		num_words = count_words(full_book)
		num_chars = count_characters(full_book)
		sorted_dict = sort_on(num_chars)
		print("============ BOOKBOT ============")
		print("Analyzing book found at books/frankenstein.txt...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for char in sorted_dict:
			count = sorted_dict[char]
			print(f"{char}: {count}")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

main()
