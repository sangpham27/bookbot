def get_num_words(text):
    words = text.split()
    return len(words)


#
# Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
# Convert any character to lowercase using the .lower() method, we don't want duplicates.
# Use a dictionary of String -> Integer. The returned dictionary should look something like this:
# {
#     'a': 5,
#     'b': 2,
#     'c': 3,
#     ...
# }

def get_char_frequency(text):
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Use the .sort() method:
# Use a helper function to return the "num" key of each dictionary for comparison.
# Sort the list from greatest to least by the count.

def sort_on(items):
    return items["num"]

def get_sorted_char_frequency(char_freq):
    sorted_freq = []
    for char, num in char_freq.items():
        sorted_freq.append({"char": char, "num": num})
    sorted_freq.sort(key=sort_on, reverse=True)
    # I want to return the char_freq dictionary as a list of dictionaries sorted by the "num" key in descending order.
    sorted_char_frq = {}
    for item in sorted_freq:
        sorted_char_frq[item["char"]] = item["num"]
    return sorted_char_frq
