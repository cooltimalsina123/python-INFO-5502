# Write a Python program to find maximum and the minimum value in a set

def find_max_min(provided_set):
    max_value = max(provided_set)
    min_value = min(provided_set)

    return 'max_value: ' + str(max_value) + ' and ' + 'min_value: ' + str(min_value)


print(find_max_min([4, 2, 5, 8]))
