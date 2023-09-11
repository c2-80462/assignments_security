def calculate_compound_interest(p, t, ci):
    compoundInterest = (p * (1 + ci/100) ** t) - p
    print(f"CI is {compoundInterest}")
    print(f"total amount payable is {p + compoundInterest} in {t} years")


p = float(input("Enter the principal amount. "))
t = float(input("Enter the time period. "))
ci = float(input("Enter the rate of Compound Interest. "))
calculate_compound_interest(p, t, ci)
