def avg(n1, n2, n3):
    average=(n1 + n2 + n3) / 3
    return average


print("enter 3 numbers to find their average")
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))


result = avg(n1, n2, n3)
print(f"The average is {result}")
