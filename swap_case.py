def swap_case(string):
    # create a variable to store the new string
    # create set of lowercase characters
    # create set of uppercase characters
    # loop throu the given string
    # if char is lower
    # change char to upper then add to new string
    # elif char is upper
    # change char to lower then add it to new string
    # else char is not upper or lower
    # add char to new string
    # return new string

    # create a variable to store the new string
    changed_str = ""
    # create string of lowercase characters
    lower = "abcdefghijklmnopqrstuvwxyz"
    # create string of uppercase characters
    upper = lower.upper()
    # loop throu the given string
    for char in string:
        # if char is lower
        if char in lower:
            # change char to upper then add to new string
            changed_str += char.upper()
        # elif char is upper
        elif char in upper:
            # change char to lower then add it to new string
            changed_str += char.lower()
        # else char is not upper or lower
        else:
            # add char to new string
            changed_str += char

    # return new string
    print(changed_str)
