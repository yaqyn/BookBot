#COUNT

def get_book_count(file_contents):
    words = file_contents.split()
    wc = len(words)

    return wc


#DICT

def get_book_dict(file_contents):
    all_letters = file_contents.lower()
    letters_dict = {}
    letter_counter = 0
    for letter in all_letters:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] = letters_dict[letter] + 1
    return letters_dict


#SORT

def sort_on(letters_dict):
    return letters_dict[1]

def chars_dict_sorted_list(letters_dict):
    sorted_list = []
    for letter in letters_dict:
        count = letters_dict[letter]
        sorted_list.append((letter, count))
    letters_sort = sorted(sorted_list, reverse = True, key=sort_on)
    return letters_sort
