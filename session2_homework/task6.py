# Task 6: Age Group Classifier
# Ask the user for their age and classify them into a group: (Age range is from 0 - 120)
# 0 - 12 → "Child"
# 13 - 19 → "Teenager"
# 20 - 59 → "Adult"
# 60 and above → "Senior Citizen"

age = int(input("Please enter your age: "))

if age >= 0 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 59:
    print("You are an adult")
elif age >= 60 and age <= 120:
    print("You are a senior citizen")
else:
    print("Error. Please enter your correct age")