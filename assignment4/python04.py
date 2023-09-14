# Write a method in python to display the elements of list thrice if it is a
# number and display
# the element terminated with ‘#’ if it is not a number.
# Hint-: Use InBuilt Function isdigit()
# Refer below as a input:-
# mylist = [’41’,’DROND’,’Sunbeam’, ’13’,’ZARA’]

def display_elements(mylist):
    for element in mylist:
        if element.isdigit():
            print(f"{element} " * 3)
        else:
            # If it's not a number, display it with a '#' appended
            print(f"{element}#")

# Example usage:
mylist = ['41', 'DROND', 'Sunbeam', '13', 'ZARA']
display_elements(mylist)
