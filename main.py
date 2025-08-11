
from stats import word_counter
from stats import charecter_counter
from stats import get_book_text
from stats import dic_sort


def main(file_path):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {file_path}...")
    print("----------- Word Count ----------")
    amount_of_words = word_counter(file_path)
    print(f"Found {amount_of_words} total words")
    print("--------- Character Count -------")
    mess_list= dic_sort(file_path)
    new_list= []

    for i in mess_list:
        if i["char"].isalpha():
            new_list.append(i)
    
    for i in new_list:
        print(f"{i["char"]}: {i["num"]}")
    
    
        
    



if __name__ == "__main__":
    main("books/frankenstein.txt")



