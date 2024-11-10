number = int(input("Enter a number: "))

reverse = 0

while number != 0:
    last_digit = number % 10  
    reverse = reverse * 10 + last_digit  
    number //= 10  

print(f"The reverse of the number is: {reverse}")
