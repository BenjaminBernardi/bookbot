from stats import get_number_of_words
from stats import get_number_of_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("/home/aemulus/projects/bookbot/books/frankenstein.txt")
    number_words = get_number_of_words(book_text)
    number_characters = get_number_of_characters(book_text)
    print(f"{number_words} words found in the document")
    print(number_characters)

main()