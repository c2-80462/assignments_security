# Write a program in Python to read a string from the keyboard. Replace each ‘this’ word
# with ‘that word’ in this String. Example: this is me and this is my python program.
# Output: That is me and That is my python program

def function1():
    str_input = ("this is me and this is my python program")
    replace = str_input.replace("this", "that")
    print(replace)


function1()