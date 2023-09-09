def maximum(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f"The largest number is {n1}")
        return n1


    elif n2 > n1 and n2 > n3:
        print(f"The largest number is {n2}")
        return n2


    elif n3 > n1 and n3 > n2:
        print(f"The largest number is {n3}")
        return n3


n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))

result = maximum(n1, n2, n3)
