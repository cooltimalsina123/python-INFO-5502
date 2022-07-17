# Write a Python program to sum all the items in a list

def list_to_sum(numbers):
    sum_result = 0
    for x in numbers:
        sum_result += x
    return sum_result


print(list_to_sum([1, 2, 3, 4]))
