
day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "monday":
    if time == "morning":
        print("Suggestion: You should eat breakfast and go to work!")
    elif time == "afternoon":
        print("Suggestion: You should eat lunch and go for a walk!")
    elif time == "evening":
        print("Suggestion: You should eat dinner and relax!")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

elif day == "friday":
    if time == "morning":
        print("Suggestion: You should go to yoga class!")
    elif time == "afternoon":
        print("Suggestion: You should study!")
    elif time == "evening":
        print("Suggestion: You should go out with friends!")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

elif day == "sunday":
    if time == "morning":
        print("Suggestion: You should go to church!")
    elif time == "afternoon":
        print("Suggestion: You should meal prep!")
    elif time == "evening":
        print("Suggestion: You should relax and get ready for the week!")
    else:
        print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")

else:
    print("Sorry, I don't recognize that day. Try: Monday, Friday, Sunday...")