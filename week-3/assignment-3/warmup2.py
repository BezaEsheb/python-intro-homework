age = int(input("What is your age: "))

age_range = ""

if 0 < age <= 12:
    age_range = "Child"
elif 12 < age <= 17:
    age_range = "Teen"
elif 17 < age <= 64:
    age_range = "Adult"
else:
    age_range = "Senior"

print(f"Age range: {age_range}")
