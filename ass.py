num = input("input a number")
num = int(num)

if 300 > num > 200:
    print(f"{num} is less than 300 but greater than 200")
elif 200 > num > 100:
    print(f"{num} is less than 200 but greater than 100")
elif num < 100:
    print(f"{num} is less than 100")
else:
    pass
# use pass if you want to keep a block empty
