import tkinter as tk
import re

def check_password_strength(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")

    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")

    if not re.search(r'[0-9]', password):
        suggestions.append("Include at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character.")

    if len(suggestions) == 0:
        strength = "Strong"
        suggestion_text = "No suggestions. Great password!"
    elif len(suggestions) <= 2:
        strength = "Moderate"
        suggestion_text = "\n".join(suggestions)
    else:
        strength = "Weak"
        suggestion_text = "\n".join(suggestions)

    return strength, suggestion_text

def on_check_strength():
    password = entry.get()
    strength, suggestion_text = check_password_strength(password)
    strength_label.config(text=f"Strength: {strength}")
    suggestion_label.config(text=suggestion_text)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter your password:").pack(pady=10)
entry = tk.Entry(root, show='*', width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=on_check_strength).pack(pady=10)

strength_label = tk.Label(root, text="Strength: ")
strength_label.pack()

suggestion_label = tk.Label(root, text="", wraplength=350, justify="left")
suggestion_label.pack()

root.mainloop()
