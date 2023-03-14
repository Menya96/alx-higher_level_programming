#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if my_list:
        for i in my_list:
            " ".join(str(i) for i in my_list) 
            print("{:d}".format(i))   
