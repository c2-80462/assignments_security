# Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit
# price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for
# quantities over 50.


quote = 0
quantity = float(input("Enter the quantity you want to buy"))

rate_1 = quantity * 5
rate_2 = 150 + ((quantity - 30) * (5 - 5 * 0.10))
rate_3 = 240 + ((quantity - 50) * (5 - 5 * 0.15))

if quantity <= 30:
    quote = rate_1

elif 30 < quantity <= 50:
    quote = rate_2

else:
    quote = rate_3

print(f"The quote for {quantity} quantity is {quote}.")
