# (3) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '\$', except the first char itself. (6 points)
# Sample String : 'restart',
# Expected Result : 'resta\$t'

def given_string(string_provided):
    first_value = string_provided[0]
    removed_value = string_provided[1:]
    removed_value = removed_value.replace(first_value, '\\$')
    return first_value+removed_value


print(given_string('restart'))
