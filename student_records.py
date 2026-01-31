import json

students = {
    "101": {"name": "Alice", "age": 20, "course": "Python"},
    "102": {"name": "Bob", "age": 22, "course": "Data Science"},
    "103": {"name": "Charlie", "age": 21, "course": "AI"}
}

students["102"]["age"] = 23
students["104"] = {"name": "David", "age": 19, "course": "ML"}
del students["103"]

for sid, details in students.items():
    print(sid, details)

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

with open("students.json", "r") as f:
    loaded_students = json.load(f)

print("\nFormatted Student Records\n")
for sid, details in loaded_students.items():
    print(f"ID: {sid}")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Course: {details['course']}")
    print("-" * 20)
