"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. Given a string (s), 
which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.
- If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G,O,E.
"""


def company_logo(s):
    # Print 3 common characters and the number of characters
    # Sort in decending order of the number of characters
    # if the number is the same sort characters in alphabetical order

    # psydo
    unsorted = []
    nums = []
    s = list(s)
    s.sort()
    # loop through the string
    for char in s:
        # if char count is more than 1 add to dictionary with the count
        count = s.count(char)
        if count > 1 and char not in unsorted:
            unsorted.append(char)
            nums.append(count)

    print(unsorted, nums)
    # loop throu the dict
    # if


company_logo("sfklhsfienfsdgjsdjldlfj")
