year = int(input("Enter a year"))

if year % 100 == 0 and year % 400 != 0:
    print(f"The year {year} is not a leap year")

elif year % 4 == 0 or year % 400 == 0:
    print(f"The year {year} is a leap year")

else:
    print(f"The year {year} is not a leap year")
