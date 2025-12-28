import os
import re

os.system('cls')


def is_valid_login(username, password):
    valid_username = "admin"
    valid_password = "12345"

    if "'" in username or "'" in password:
        print("[!] Security Alert: Possible SQL Injection attempt detected.")
        return False

    return username == valid_username and password == valid_password


def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search(r"[a-z]", password):
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Weak"
    if not re.search(r"[0-9]", password):
        return "Weak"
    if not re.search(r"[!,@,#,$,%,&]", password):
        return "Weak"
    return "Strong"


def login(username, password):
    strength = check_password_strength(password)

    if not is_valid_login(username, password):
        return f"Login failed. Password strength: {strength}"

    return f"Login successful. Password strength: {strength}"


if __name__ == "__main__":
    print("🔐 Login System Test\n")
    username = input("👤 Enter Username: ").strip()
    password = input("🔑 Enter Password: ").strip()

    result = login(username, password)
    print("\n📤 Result:")
    print(result)

