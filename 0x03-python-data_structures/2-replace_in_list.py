#!usr/bin/pyhton3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    
    length = len(my_list)
    
    if idx > length - 1:
        return (my_list)
    
    my_list.pop(idx)
    my_list.insert(idx, element)
    return (my_list)
