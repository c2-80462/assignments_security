# Concatenate two lists in the following order by using list comprehension
# Input:- list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for l1 in list1:
    for l2 in list2:
        result.append(l1 + l2)

print(result)
