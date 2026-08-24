from stats import get_book_count
from stats import get_book_dict
from stats import sort_on
from stats import chars_dict_sorted_list
import sys

#TEXT
def get_book_text(PATH_TO_BOOK):
    with open(PATH_TO_BOOK) as f:
        file_contents = f.read()
    return file_contents

def print_report (book_path, wc, letters_sort):
    print (f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print (f"----------- Word Count ----------\nFound {wc} total words")
    print ("--------- Character Count -------")
    for letter, count in letters_sort:
        if letter.isalpha():
            print(f"{letter}: {count}")
        else:
            continue
    print ("============= END ===============")
#MAIN
def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    words = get_book_count(book)
    letters_dict = get_book_dict(book)
    letters_sort = chars_dict_sorted_list(letters_dict)
    print_report(sys.argv[1], words, letters_sort)


# start
main()
