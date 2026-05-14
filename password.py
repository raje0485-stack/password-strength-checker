import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1

    # Number check
    if re.search(r"[0-9]", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength result
    if score == 5:
        return "Very Strong 💪"
    elif score >= 4:
        return "Strong ✅"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

# User input
password = input("Enter your password: ")

result = check_password_strength(password)

print(f"Password Strength: {result}")
