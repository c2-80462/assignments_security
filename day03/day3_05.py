# 5)Define a function overlapping() that takes two lists and returns True if they
# have at least one member in common, False otherwise.

def overlapping(list1, list2):
    for element1 in list1:
       for element2 in list2:
            if element1 == element2:
                return True
            else:
                return False

user_input1 = input("Enter the first list")
list1 = user_input1

user_input2 = input("Enter the second list")
list2 = user_input2

if overlapping(list1, list2):
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")

