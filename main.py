
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_book_text(text)
    char_count = count_char(text)
    # print(text)
    # print(word_count)
    # print(char_count)
    char_report = \
f"""--- Begin report of books/frankenstein.txt ---
{word_count} words found in the document 

"""
    
    for char in char_count:
        char_report += f"The '{char}' character was found {char_count[char]} times \n"

    char_report += "--- End report ---"
    print (char_report)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_book_text(text):
    words = text.split()
    return len(words)

def count_char(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char.isalpha():
            if char == "\n":
                char = "\\n"
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    char_dict_sorted = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    return char_dict_sorted





main()