# Input from the user
temperature = float(input("Enter the temperature in Celsius: "))

# Check the temperature range
if temperature <= 0:
    print("The temperature is freezing.")
elif 0 < temperature <= 25:
    print("The temperature is moderate.")
else:
    print("The temperature is hot.")
