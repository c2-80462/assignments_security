def maxnum():
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the biggest number")

    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the biggest number")

    else:
        print(f"{num3} is the biggest number")


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

maxnum()