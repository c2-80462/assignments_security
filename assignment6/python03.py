# Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string

def string():
    up = 0
    down = 0
    num = 0
    white = 0
    string = str(input("Enter a string. "))
    for s in string:
        if s.isupper():
            up += + 1
        elif s.islower():
            down += 1
        elif s.isdigit():
            num += 1
        else:
            white += 1

    print(f"The string is {string}")
    print(f"The number of uppercase characters are {up}")
    print(f"The number of lowercase characters are {down}")
    print(f"The number of digits are {num}")
    print(f"The number of whitespaces are {white}")


string()