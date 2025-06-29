import re

def check_password_strength(password):
    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*()_+]", password) is None

    errors = [length_error, upper_error, lower_error, digit_error, special_error]
    strength = "Strong" if not any(errors) else "Weak"
    return strength

password = input("Enter password to check: ")
print("Password Strength:", check_password_strength(password))