students = [
    {"id":1, "name":"Jayrajsinh","marks":89},
    {"id":2, "name":"Hirenbhai","marks":99}
]

sid = int(input("Enter Your Id: "))
name = input("Enter Student name: ")
marks = int(input("Enter Your Marks"))

new_student = {
    "id": sid,
    "name": name,
    "marks":marks
}

students.append(new_student)

print("Updated Student List")
print(students)