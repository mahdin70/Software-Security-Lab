try:
    user_input = input("Enter a string (up to 5 characters): ").strip()

    if len(user_input) > 5:
        raise ValueError("Input string must be at most 5 characters long.")
    if not user_input:
        raise ValueError("Input string cannot be empty.")

    with open("top-100k-password-list.txt", "r") as file:
        passwords = file.readlines()

    filtered_passwords = [password.strip() for password in passwords if user_input not in password]

    if filtered_passwords:
        print("Passwords that do not contain '{}' as a substring:".format(user_input))
        for password in filtered_passwords:
            print(password)
    else:
        print("No password contains '{}' as a substring.".format(user_input))

except FileNotFoundError:
    print("File not found: top-100k-password-list.txt")
except ValueError as ve:
    print("Input error:", str(ve))
except Exception as e:
    print("An error occurred:", str(e))
