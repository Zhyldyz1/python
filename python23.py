def check_discount_eligibility(age, is_member):
    if age < 0:
        return "Invalid age"
    elif age < 12:
        return "Eligible for child discount"
    elif age >= 65:
        return "Eligible for senior discount"
    elif is_member:
        return "Eligible for membership discount"
    else:
        return "No discount available"

# Example usage
user_age = 30
user_is_member = True

result = check_discount_eligibility(user_age, user_is_member)
print(result)
