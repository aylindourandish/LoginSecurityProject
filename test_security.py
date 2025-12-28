import os;os.system('cls')
from main import is_valid_login

print("🔐 Security Test Console (type 'exit' to stop)\n")

while True:
    username = input("👤 Enter test username: ").strip()
    if username.lower() == "exit":
        print("🛑 Exiting test mode.")
        break

    password = input("🔑 Enter test password: ").strip()
    if password.lower() == "exit":
        print("🛑 Exiting test mode.")
        break

    print("\n--- Test Result ---")
    if is_valid_login(username, password):
        print("✅ Login successful.")
    else:
        print("❌ Login failed (invalid credentials or blocked for security reasons).")
    print("-------------------\n")

