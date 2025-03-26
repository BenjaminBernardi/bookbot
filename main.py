import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_chars_by_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(path_to_book)
    number_words = get_number_of_words(book_text)
    number_characters = get_number_of_characters(book_text)
    sort_characters = sort_chars_by_count(number_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {number_words} total words")
    print("--------- Character Count -------")

    for char_dict in sort_characters:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()