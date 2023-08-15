#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0 or idx > (len(my_list)-1):
        return my_list.copy()
    else:
        neu_list = [numb for numb in my_list.copy()]
        neu_list[idx] = element
        return neu_list
