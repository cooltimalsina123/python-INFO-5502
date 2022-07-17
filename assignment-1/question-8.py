# Write a Python program to find the duplicate elements in a given array of integers. Return -1 If there are no such elements.

def find_duplicate(arr):
    check_value = set()
    result = []
    for x in arr:
        if x in check_value:
            result.append(x)
        else:
            check_value.add(x)

    return result


print(find_duplicate([1, 2, 3, 5, 2, 5]))
