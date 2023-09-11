calls = float(input("Enter total number of calls"))

rate1 = 200
rate2 = 0.60
rate3 = 0.50
rate4 = 0.40

bill = 0

if calls < 100:
    bill = rate1

elif 100 < calls <= 150:
    bill = rate1 + (calls - 100) * rate2

elif 150 < calls <= 200:
    bill = rate1 + (rate2 * 50) + (calls - 150) * rate3

elif 200 < calls:
    bill = rate1 + (rate2 * 50) + (rate3 * 50) + (calls - 200) * rate4

print(f"The bill is Rs.{bill}")