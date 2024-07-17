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
