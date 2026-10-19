students = [
    {"id": 1, "name": "Alice", "marks": 85},
    {"id": 2, "name": "Bob", "marks": 78},
    {"id": 3, "name": "Charlie", "marks": 92}
]

sid = int(input("Enter student ID to search: "))

found = False

for student in students:
    if student["id"] == sid:
        print("Student details:", student)
        found = True
        break

if not found:
    print("Student not found.")