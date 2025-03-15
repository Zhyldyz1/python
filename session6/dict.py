students = {
    "101": {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "courses": ["Math", "Physics", "Computer Science"],
        "attendance": 95
    },
    "102": {
        "name": "Bob Smith",
        "age": 21,
        "grade": "B",
        "courses": ["History", "Literature", "Political Science"],
        "attendance": 88
    },
    "103": {
        "name": "Charlie Brown",
        "age": 19,
        "grade": "A-",
        "courses": ["Biology", "Chemistry", "Physics"],
        "attendance": 92
    },
    "104": {
        "name": "Diana Adams",
        "age": 22,
        "grade": "C+",
        "courses": ["Economics", "Statistics", "Business"],
        "attendance": 80
    },
    "105": {
        "name": "Ethan Green",
        "age": 20,
        "grade": "B+",
        "courses": ["Computer Science", "Mathematics"],
        "attendance": 90
    }
}

# Task1: Prints the user id and name of the student in the following format
# 101: Alice Johnson
# 102: Bob Smith
# ...
# 105: Ethan Green

# for key, value in students.items():
#     print(f"{key}: {value['name']}")

# Task 2:
# Print only students that grades are A (A-, A)
# 101: Alice Johnson
# 103: Charlie Brown

# for key, value in students.items():
#     print(f"{key}: {value['name']}")

# print("\nStudents with grades A or A-:")

# Task 2: Print students with grades A or A-
# for key, value in students.items():
#     if "A" in value["grade"]:
#         print(f"{key}: {value['name']}")

# Task 3:
# Ask user for an input of course
# Print the students that are taking this course
# Input: Computer Science
# Output:
# 101: Alice Johnson
# 105: Ethan Green
inp = input("Input: ").lower()

for key, value in students.items():
    for elem in value["courses"]:
       if inp == elem.lower():
         print(f"{key}: {value['name']}")
