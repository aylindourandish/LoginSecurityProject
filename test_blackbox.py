import os;os.system('cls')
from main import login, check_password_strength

def black_box_test():

    print(" Black Box Test: Validating Program's Judgment")
   

    test_count = 1

    while True:
        
        username = input("\n Enter username: ").strip()
        password = input(" Enter password: ").strip()

        print(f"\n ---  Test Case #{test_count} ---")
        expected_strength = check_password_strength(password)
        output = login(username, password)

        print("\n Program Output:")
        print(f"       {output}")

        if f"Password strength: {expected_strength}" in output:
            print(" Test Result: PASSED (Program judged password correctly)\n")
        else:
            print(" Test Result: FAILED (Program misjudged password strength)\n")

        print(" Test Finished. Starting next test...\n\n")
        print("-------------------\n")
        test_count += 1

if __name__ == "__main__":
    black_box_test()
