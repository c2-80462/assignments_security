# 2)Write a program that accepts a list from user and print the alternate element
# of list.
def function1():
    list1 = []
    print("Enter elements for list ")
    for index in range(5):
        elements1 = input("Enter elements: ")
        list1.append(elements1)


    print_element = True


    print("Alternate elements of the list:")
    for element in list1:
        if print_element:
            print(element)
        print_element = not print_element

function1()
