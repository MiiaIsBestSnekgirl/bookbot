def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main(file_path):
    full_text = get_book_text(file_path)
    print(full_text)


def word_counter(file_path):
    full_text = get_book_text(file_path)
    word_list = full_text.split()
    
    print(f"{len(word_list)} words found in the document")

    


word_counter("books/frankenstein.txt")