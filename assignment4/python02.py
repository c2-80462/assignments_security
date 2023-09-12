# 2)Wirite a Python Program to find the repeated item of a tuple(Take a value
# from user which you want to find)
def function1():
    t1 = 1, 2, 3, 4, 5, 4, 3, 2, 1
    print({t1})
    item = int(input("Find how many times a number is repeated"))
    repeat = t1.count(item)
    print(f"{item} has been repeated {repeat} times")

function1()



