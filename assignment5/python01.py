# 1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
#  Sort and print students and their favourite colours alphabetically by name
#D. Create a list, put all keys in it, use sort function

def function1():
    people={'Arham':'Blue', 'Lisa':'Yellow', 'Vinod':'Purple', 'Jenny':'Pink'}
    people["Lisa"] = "Pink"
    keys = people.keys()
    keys = list(keys)
    keys.sort()
    print(keys)
    people.pop('Jenny')
    print(people)



function1()