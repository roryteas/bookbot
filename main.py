book_path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return(file_contents)

def get_book_charcounts(booktext):
    lower = booktext.lower()
    char_dict = {}
    for char in lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_book_wordcount(booktext):

    return len(booktext.split())
def sort_on(dict):
    return dict["num"]
def book_report(path):
    print(f"--- Begin report of {path} ---")
    booktext = get_book_text(book_path)
    print(f"{get_book_wordcount(booktext)} words found in the document")
    print("\n")
    charcountsdict = get_book_charcounts(booktext)
    charcounts = []
    for item in charcountsdict:
        charcounts.append({"char": item, "num": charcountsdict[item]})
    charcounts.sort(reverse=True, key=sort_on)
    for char in charcounts:
        print(f"The '{char}' character was found {char["num"]} times")
    print("--- End Report ---")
        
def main():
    #print(booktext)
    book_report(book_path)
    #print(get_book_wordcount(booktext))
    return

main()