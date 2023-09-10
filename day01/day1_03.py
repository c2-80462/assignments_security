num = int(input("Enter a 4 digit number"))

unit = num % 10
tens = (num % 100) - unit
hundreds = (num % 1000) - (tens + unit)
thousands = (num % 10000) - (hundreds + tens + unit)

print(f"Face values are: {thousands//1000} {hundreds//100} {tens//10} {unit}")
print(f"Place values are: {num} = {thousands} + {hundreds} + {tens} + {unit}")
print(f"Reversed values are: {unit//1}{tens//10}{hundreds//100}{thousands//1000}")
