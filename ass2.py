# get age input from user and check if user is eligible for voting
# get kms input from user and convert it into miles and metres

age = input("Enter your age:")
age = int(age)

if age >= 18:
    print("You're eligible for voting")
else:
    print("You're not eligible for voting")

kms = input("Enter distance in kms")
kms = int(kms)

miles = kms / 1.609
print(f"{kms} kms is {miles} miles")
