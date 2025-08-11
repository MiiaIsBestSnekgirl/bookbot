

def word_counter(file_path):
    
    full_text = get_book_text(file_path)
    word_list = full_text.split()
    return len(word_list)
    





def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def charecter_counter(file_path):
    full_text = get_book_text(file_path)
    charecter_instances= {

    }
    for i in full_text.lower():
            if i not in charecter_instances:
                charecter_instances[i] = 1
            else:
                charecter_instances[i] += 1
    return charecter_instances


def dic_sort(file_path):
    unsorted=charecter_counter(file_path)
    sorted_list= [

    ]
    for char in unsorted:
        amount= unsorted[char]
        new_dic= {
            "char": char, "num": amount
        }
        sorted_list.append(new_dic)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
       
def sort_on(items):
    return items["num"]










        

    
 


     
    
            



        

