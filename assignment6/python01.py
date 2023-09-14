# Write a menu Driven Program To Calculate the perimeter and Area of
# different Shapes(Circle,Square,Rectangle) using functions

def circle():
    r = float(input("Enter the radius of the circle "))
    circumference = 2 * 3.14 * r
    area = 3.14 * (r**2)
    print(f"For radius {r}, the area is {area} and the circumference is {circumference}")


def square():
    s = float(input("Enter the side of the square "))
    perimeter = 4 * s
    area = s**2
    print(f"For {s}, the area is {area} and the perimeter is {perimeter}")


def rectangle():
    l = float(input("Enter the length "))
    b = float(input("Enter the breadth "))
    perimeter = (2 * l) + (2 * b)
    area = l * b
    print(f"For {l} and {b}, the area is {area} and the perimeter is {perimeter}")


def menu():
    print("-" * 20)
    print("Welcome to menu. ")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")
    print("-" * 20)

    choice = int(input("Enter a choice. "))
    return choice


while True:
    ch = menu()

    if ch==1:
        circle()
    elif ch==2:
        square()
    elif ch==3:
        rectangle()
    elif ch==4:
        print("Thank You")
        break
    else:
        print("Enter a valid input.")
