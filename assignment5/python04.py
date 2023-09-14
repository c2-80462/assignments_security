# Write a program in Python to find out the frequency of each number in stored in a list
# using a python dictionary.
# Example
# List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]
# Output ={1: 1, 2:2,3:1,4:4,5:1,6:2,7:7,23:1}


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]

frequency = {}

for num in list1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print the frequency dictionary
print("Output =", frequency)
