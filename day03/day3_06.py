# 6)Find and display the largest number of a list without using built-in function
# max(). Your program should ask the user to input values in list from keyboard.

n = int(input("Enter the number of values in the list: "))
user_list = []

for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    user_list.append(value)

largest = user_list[0]

for num in user_list:
    if num > largest:
        largest = num

print(f"The largest number in the list is: {largest}")
