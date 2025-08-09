

def word_counter(file_path):
    full_text = get_book_text(file_path)
    word_list = full_text.split()
    print(f"{len(word_list)} words found in the document")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def charecter_counter(file_path):
    full_text = get_book_text(file_path)
    charecter_instances= {

    }
    for i in full_text:
        for L in i:
            L = L.lower()
            if L not in charecter_instances:
                charecter_instances[L] = 1
            else:
                charecter_instances[L] += 1
    return charecter_instances
     
    
            
charecter_counter("books/frankenstein.txt")

        

