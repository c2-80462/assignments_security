def avg_grade():
    grade = (sub1 + sub2 + sub3) / 3
    if 90 <= grade:
        print(f"Your average is {grade} and your grade is A.")

    elif 80 < grade <= 89:
        print(f"Your average is {grade} and your grade is B.")

    elif 70 < grade <= 79:
        print(f"Your average is {grade} and your grade is C.")

    elif 60 < grade <= 69:
        print(f"Your average is {grade} and your grade is D.")

    elif grade <= 59:
        print(f"Your average is {grade} and your grade is F.")


sub1 = int(input("Enter your marks for sub1 out of 100 "))
sub2 = int(input("Enter your marks for sub2 out of 100 "))
sub3 = int(input("Enter your marks for sub3 out of 100 "))

avg_grade()
