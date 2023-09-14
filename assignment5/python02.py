# 2) Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}
# Expected output
# Result: 500

def function1():

    sum = 0
    dict1 = {'key1': 200, 'key2': 300}
    for value in dict1.values():
        sum+=value

    print(sum)


function1()