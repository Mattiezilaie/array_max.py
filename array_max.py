# Author: Mahtab Zilaie
# Date: February 10, 2020
# Description: recursive function that takes a list of numbers and the returns max/biggest value in the list


def rec_array_max(lst, n):
    """helper function searches in list for max number"""

    if n == 0:
        return lst[0]    # if len of list is only 1, returns that value

    return max(lst[n], rec_array_max(lst, n - 1)) # compares value in last index to the second to last value


def array_max(lst):
    """sets n to last item's index"""
    return rec_array_max(lst, n=len(lst) - 1)



#print(array_max([1, 2, 4]))

# rec_array_max(lst, 2)
# (4, rec_array_max(lst, 1)) => max(2, rec_array_max(lst, 0)) => 1

# max_element = lst[0]
#
# for i in range(1, n):
#     max_element = max(max_element, lst[0])



