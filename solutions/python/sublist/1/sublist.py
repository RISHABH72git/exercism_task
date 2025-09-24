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
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    elif is_sublist(list_one, list_two):
        return SUBLIST
    else:
        return UNEQUAL

def is_sublist(list_one, list_two):
    if not list_one:
        return True
    for i in range(len(list_two)-len(list_one)+1):
        if list_two[i:i+len(list_one)] == list_one:
            return True
    return False 