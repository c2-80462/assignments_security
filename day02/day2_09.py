def calculate_simple_interest(p, t, si):
    simpleInterest = (p * t * si) / 100
    print(f"SI is {simpleInterest}")
    print(f"total amount payable is {p+simpleInterest} in {t} years")


p = float(input("Enter the principal amount. "))
t = float(input("Enter the time period. "))
si = float(input("Enter the rate of Simple Interest. "))
calculate_simple_interest(p, t, si)