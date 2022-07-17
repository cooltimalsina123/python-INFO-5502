# Write a Python program to count the number of characters in a string

def given_string(provided_string):
    char_repeated = {}
    for x in provided_string:
        if x in char_repeated:
            char_repeated[x] += 1
        else:
            char_repeated[x] = 1
    return char_repeated


print(given_string('google'))
