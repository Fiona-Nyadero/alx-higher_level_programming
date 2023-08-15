#!/usr/bin/python3

def no_c(my_string):
    neu_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            neu_string += char
    return neu_string
