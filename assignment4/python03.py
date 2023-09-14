# Write a Python program to count the elements in a list until an element is a
# tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3


list = [10, 20, 30, (40, 50), 60]
count = 0

for element in list:
    if type(element) == tuple:
        break
    count += 1

print("Number of elements until a tuple is found:", count)

