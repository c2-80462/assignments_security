# Display following menu and write required function for it
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times


def display_even_characters(input_string):
    result = ""
    for i in range(1, len(input_string), 2):
        result += input_string[i]
    return result


def display_odd_characters(input_string):
    result = ""
    for i in range(0, len(input_string), 2):
        result += input_string[i]
    return result


def display_length(input_string):
    return len(input_string)


def add_a_to_end(input_string):
    return input_string + 'a' * len(input_string)


print("Menu:")
print("A. Display characters from even position")
print("B. Display characters from odd position")
print("C. Display length of a string")
print("D. Add 'a' at the end of string length times")


user_input = input("Enter a string: ")

# Ask the user to select an option
choice = input("Select an option (A/B/C/D): ")

# Perform the selected operation and display the result
if choice == 'A':
    result = display_even_characters(user_input)
    print("Characters from even position:", result)
elif choice == 'B':
    result = display_odd_characters(user_input)
    print("Characters from odd position:", result)
elif choice == 'C':
    result = display_length(user_input)
    print("Length of the string:", result)
elif choice == 'D':
    result = add_a_to_end(user_input)
    print("String with 'a' added at the end:", result)
else:
    print("Invalid option. Please select A, B, C, or D.")




