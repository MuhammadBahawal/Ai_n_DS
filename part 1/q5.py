percentage = float(input("Enter your grade percentage: "))

if 90 <= percentage <= 100:
    print("Your grade is A.")
elif 80 <= percentage < 90:
    print("Your grade is B.")
elif 70 <= percentage < 80:
    print("Your grade is C.")
elif 60 <= percentage < 70:
    print("Your grade is D.")
else:
    print("Your grade is F.")
