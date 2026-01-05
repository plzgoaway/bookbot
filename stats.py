def count_words(input_string):
    counter = 0
    num_of_words = input_string.split()
    for word in num_of_words:
        counter += 1
    return f"Found {counter} total words"


def count_chars(input_text):
    char_dict = {}
    for char in input_text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        elif char not in char_dict:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]



def sort_report(dict_of_chars):
    count_dict = []
    for char, num in dict_of_chars.items():
        new_dict = {"char": char, "num": num }
        count_dict.append(new_dict)
    count_dict.sort(reverse=True, key=sort_on)
    return count_dict






