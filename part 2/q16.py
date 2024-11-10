number = int(input("Enter an integer: "))

digit_sum = 0

while number != 0:
    digit_sum += number % 10 
    number //= 10  

print(f"The sum of the digits is: {digit_sum}")
