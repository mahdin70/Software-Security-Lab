try:
    with open("top-100k-password-list.txt", "r") as file:
        passwords = file.readlines()

    filtered_passwords = []
    for password in passwords:
        hasDigit = any(char.isdigit() for char in password)
        if not hasDigit:
            filtered_passwords.append(password.strip())
                
    if filtered_passwords:
        with open("Dummy_Passwords.txt", "w") as output_file:
            output_file.write("\n".join(filtered_passwords))
    
    else:
        with open("Dummy_Passwords.txt", "w") as output_file:
            output_file.write("No password starts with pass")

    print("Total passwords without digits:", len(filtered_passwords))


except FileNotFoundError:
    print("File not found: top-100k-password-list.txt")
    
except Exception as e:
    print("An error occurred:", str(e))

