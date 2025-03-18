# Task 1: Filter and Count Students by Attendance
# Write a function that takes a dictionary of students and a minimum attendance percentage. The function should return a dictionary containing only the students who meet or exceed the attendance requirement.
# Example:
students_data = {
    "101": {"name": "Alice", "attendance": 95},
    "102": {"name": "Bob", "attendance": 88},
    "103": {"name": "Charlie", "attendance": 92},
    "104": {"name": "Diana", "attendance": 80},
    "105": {"name": "Ethan", "attendance": 90},
}

def filtered_students(students_data, attendance):
    result = {}
    for i, score in students_data.items():
        if score["attendance"] > 90:
            result[i] = score
    return result

print(filtered_students(students_data, 90))

# print(filter_students_by_attendance(students_data, 90))

# Output:
# {
#     "101": {"name": "Alice", "attendance": 95},
#     "103": {"name": "Charlie", "attendance": 92},
#     "105": {"name": "Ethan", "attendance": 90}
# }

