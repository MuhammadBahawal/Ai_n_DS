number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is a multiple of both 3 and 5.")
else:
    print(f"{number} is not a multiple of both 3 and 5.")
