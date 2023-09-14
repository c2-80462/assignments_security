# Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
# Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}


number_dict = {'EVEN': [], 'ODD': []}

for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        number_dict['EVEN'].append(num)
    else:
        number_dict['ODD'].append(num)


print(number_dict)
