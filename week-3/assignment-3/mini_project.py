day = input("What day is it?")
time = input("what time of day?")

if day == "Monday" and time =="morning":
    print("Suggestion: You should eat breakfast and go to work!")
elif day == "Monday" and time =="afternoon":
    print("Suggestion: You should eat lunch and go for a walk!")
elif day == "Monday" and time =="evening":
    print("Suggestion: You should eat dinner and relax!")


elif day == "Friday" and time =="morning":
    print("Suggestion: You should go to yoga class!")
elif day == "Friday" and time =="afternoon":
    print("Suggestion: You should study!")
elif day == "Friday" and time =="evening":
    print("Suggestion: You should go out with friends!")

elif day == "Sunday" and time =="morning":
    print("Suggestion: You should go to church!")
elif day == "Sunday" and time =="afternoon":
    print("Suggestion: You should meal prep!")
elif day == "Sunday" and time =="evening":
    print("Suggestion: You should relax and get ready for the week!")
else:
    print("Suggestion: Sorry, I don't recognize that day. Try: Monday, Friday, Sunday...!")