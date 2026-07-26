age = int(input("Enter your age: "))

age_range = ""

if age >= 0 and age <= 12:
    age_range = "Child"
elif age >= 13 and age <= 17:
    age_range = "Teen"
elif age >= 18 and age <= 64:
    age_range = "Adult"
else:
    age_range = "Senior"

print(f"You are a {age_range}")
