# Calculate the sum and average of the digits present in a string
# Str1="Python83737@#8496"

def calc():
    sum=0
    Str1="Python83737@#8496"
    for nums in Str1:
        if nums.isdigit() == True:
            nums = int(nums)
            sum += nums
    print(f"Total sum is {sum}")


calc()