students = {101: "Amit", 102: "Riya", 103: "John"}
inverted_students = {name: roll_number for roll_number, name in students.items()}

print(inverted_students)