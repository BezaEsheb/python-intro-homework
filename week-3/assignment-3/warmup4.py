number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is  positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero.")

if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")
