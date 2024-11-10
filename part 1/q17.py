number = int(input("Enter an integer: "))

if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by both 2 and 3.")
elif number % 2 == 0:
    print(f"{number} is divisible by 2.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 2 or 3.")
