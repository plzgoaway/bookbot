import sys
from stats import count_words, count_chars, sort_on, sort_report

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit (1)
    text_return =  get_book_text(sys.argv[1])
    num_of_words = count_words(text_return)
    chars = count_chars(text_return)
    news = sort_report(chars)
    print(num_of_words)
    for dict in news:
        carry = dict["char"]
        nummy = dict["num"]
        if carry.isalpha() == True:
            print(f"{carry}: {nummy}")
        
    




main()