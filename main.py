import sys
from stats import get_num_words
from stats import get_char_frequency
from stats import get_sorted_char_frequency
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    input_program = sys.argv
    if len(input_program) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(input_program[1])
    print(text)
    print(f"Found {get_num_words(text)} total words")
    # print(f"{get_char_frequency(text)}")
    # Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it.
    sorted_char_freq = get_sorted_char_frequency(get_char_frequency(text))
    for char, num in sorted_char_freq.items():
        if char.isalpha():
            print(f"{char}: {num}")
    # print(f"{sorted_char_freq}")
    ####
if __name__ == "__main__":
    main()