#input validation with a while loop

while True:
    try:

        user_input = int(input("Enter a positive integer: "))
        if user_input <= 0:
            print("That's not a positive integer. Try again.")
        else:
            print(f"Got it: {user_input}")
            break
    except ValueError:

        print("That's not a positive integer. Try again.")
        break
    
