number = float(input("Enter a number: "))

lower_limit = 10
upper_limit = 50

if lower_limit <= number <= upper_limit:
    print(f"The number {number} is within the range {lower_limit} to {upper_limit}.")
else:
    print(f"The number {number} is not within the range {lower_limit} to {upper_limit}.")
