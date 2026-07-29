student = {
    "name": "Bezawit Eshete",
    "grade": "A",
    "subjects": ["Math", "Biology", "History"]}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

print(student)


