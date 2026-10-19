students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78},
    {"id": 3, "name": "Charlie", "marks": 92}
]

sid = int(input("Enter student ID: "))

found = False

for student in students:
    if student["id"] == sid:
        student["marks"] = int(input("Enter new marks: "))
        found = True
        break

if found:
    print("Updated student list:")
    print(students)
else:
    print("Student not found.")