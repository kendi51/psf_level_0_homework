def merge_the_tools(strParam, factor):
    # create variable to store the strings
    # create a list to store the strings
    # loop through the string
    # if i / factor has remainder 0
    # append the storage str to the list
    # elif the character is not in the storage str - add it

    # print the list here

    # create variable to store the strings
    storage_str = ""
    # create a list to store the strings
    strings = []
    # loop through the string
    for list_index in range(len(strParam)):
        # if list_index / factor has remainder 0
        if ((list_index + 1) % factor) == 0:
            # need to check if current character is in storage str
            if strParam[list_index] not in storage_str:
                storage_str += strParam[list_index]
            # append the storage str to the list
            strings.append(storage_str)
            storage_str = ""
        # elif the character is not in the storage str - add it
        elif strParam[list_index] not in storage_str:
            storage_str += strParam[list_index]

    # print the list here
    print(*strings, sep="\n")


merge_the_tools("AABCAAADA", 3)
