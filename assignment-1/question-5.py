# Write a Python program to concatenate following dictionaries to create a new one. (6 points)
# Sample Dictionary : dic1={1:10, 2:20}, dic2={3:30, 4:40}, dic3={5:50,6:60},
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concat_dic():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}
    result = {}
    result.update(dic1)
    result.update(dic2)
    result.update(dic3)

    return result


print(concat_dic())