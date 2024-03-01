def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} no of words")
    letters = count_letters(file_contents)
    for letter in letters.keys():
        print(f"The '{letter}' character was found '{letters[letter]}' times")
    print("--- End report ---")

def count_words(book_str):
    file_list = book_str.split()
    return len(file_list)


def count_letters(book_str):
    letter_count_dict = dict()
    for letter in book_str:
        if letter != " " and letter.isalpha():
            lower = letter.lower()
            if lower in letter_count_dict.keys():
                letter_count_dict[lower] += 1
            else:
                letter_count_dict[lower] = 1
    return dict(sorted(letter_count_dict.items(), key=lambda item: item[1], reverse=True))
            
if __name__ == '__main__':
    main()
