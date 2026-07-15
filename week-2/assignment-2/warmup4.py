# What the error message said:
# TypeError: can only concatenate str (not "int") to str
#
# What caused it:
# I tried to add an integer (14) to a string ("6") without converting the string first.
#
# How you fixed it:
# I converted the string variable in the int() function to convert it to a number before adding.

# --- Code with the bug fixed ---
Value_1 = "6"
Value_2 = 14

# Fixed by converting string to an integer:
result = int(Value_1) + Value_2
print(f"The result is: {result}")