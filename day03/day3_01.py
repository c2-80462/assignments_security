# 1)Using for loop, write and run a Python program to find factorial from 0 to 10.

def factorial(n):
        result = 1
        for fact in range(1, n + 1):
            result *= fact
        return result


for num in range(11):
    result = factorial(num)
    print(f"Factorial of {num} is {result}")
