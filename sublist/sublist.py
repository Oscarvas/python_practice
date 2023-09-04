"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1 
EQUAL = 2
UNEQUAL = 3

def _is_subsequence(list_one: list, list_two: list) -> bool:

    len_list_one = len(list_one)

    if list_one == []:
        return True
    elif len_list_one < len(list_two):
        subsequence = False

        for index, element in enumerate(list_two):
            if index + len_list_one <= len(list_two): # check if the index is not out of range
                if list_one == list_two[index:index + len_list_one]:
                    subsequence = True
                    break
        return subsequence
    else:
        return False

def sublist(list_one: list, list_two: list) -> bool:

    str_one = str(list_one).strip('[]') + ','
    str_two = str(list_two).strip('[]') + ','
    
    if list_one == list_two:
        return EQUAL
    elif str_two in str_one:
        return SUPERLIST
    elif str_one in str_two:
        return SUBLIST
    else:
        return UNEQUAL