number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is  positive")
elif number < 0:
    print(f"{number} is a negative")
else:
    print(f"{number} is zero.")


#Block 2: parity check

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
