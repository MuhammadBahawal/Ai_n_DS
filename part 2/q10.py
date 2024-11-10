number = int(input("Enter an integer: "))

digit_count = 0

while number != 0:
    number //= 10  
    digit_count += 1

print(f"The number of digits is: {digit_count}")
