number = int(input("Enter a number to find its factorial: "))

factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(f"The factorial is: {factorial}")
