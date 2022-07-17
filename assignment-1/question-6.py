# Write a Python program to check whether an element exists within a tuple.

def check_value(tuple_value, elements):
    if elements in tuple_value:
        return "element exist in tuple_value"
    else:
        return "element does not exist"


print(check_value(["john", "mike"], "mike"))
