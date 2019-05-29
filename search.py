# Miscellaneous searching functions
# Made by Ethan Goodwin with reference to code by Joe Marini from Lynda.com
# Created 5/28/2019 By: Ethan Goodwin

# Learn more about algorithms here:
# https://www.lynda.com/Software-Development-tutorials/Programming-Foundations-Algorithms/718636-2.html


# Searches for an item in a list (can be unordered)
# Is less efficient then ordered search, has linear time complexity
def unordered_search(list_, item):
    for i in range(0, len(list_)):
        if item == list_[i]:
            return i
    return None


# Searches for an item in an ordered list
# Has a logarithmic  time complexity
def ordered_search(list_, item):

    list_size = len(list_) - 1

    lower_index = 0
    upper_index = list_size

    while lower_index <= upper_index:

        midpoint = (upper_index + lower_index) // 2

        if list_[midpoint] == item:
            return midpoint

        elif list_[midpoint] > item:
            upper_index = midpoint - 1

        elif list_[midpoint] < item:
            lower_index = midpoint + 1

        elif lower_index >= upper_index:
            return None

        else:  # this shouldn't ever return, but it prevents potential infinite loops
            return None
