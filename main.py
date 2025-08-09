from stats import word_counter
from stats import charecter_counter
from stats import get_book_text

    
def main(file_path):
    charecter_instances=charecter_counter(file_path)
    word_counter(file_path)
    print(charecter_instances)




    


main("books/frankenstein.txt")

