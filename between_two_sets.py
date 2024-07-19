"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
a = [2,6]
b = [24,36]

There are two numbers between the arrays: 6 and 12.
6 % 2 = 0, 6 % 6 = 0, 24%6 = 0 and 36 % 6 = 0 for the first value.
12 % 2 = 0, 12 % 6 = 0 and 24 % 12 = 0, 36 % 12 = 0  for the second value. Return 2.
"""


def get_total(a, b):
    # create a variable to store the max_value
    max_val = max(max(a, b))
    # create a variable to count
    counter = 0
    # loop through the range = i
    for i in range(1, max_val + 1):
        # create a list comprehension, check if i / num has remainder 0
        set_1 = [((i % num) == 0) for num in a]
        # create a list comprehension, check if num / i has remainder 0
        set_2 = [((num % i) == 0) for num in b]
        # test if: all list items is true:
        if all(set_1) and all(set_2):
            # if true: counter increases by 1
            counter += 1

    # return the counter
    return counter


print(get_total([1], [100]))
