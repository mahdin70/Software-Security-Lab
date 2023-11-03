import os

if len(os.sys.argv) != 3:
    print(f"{os.sys.argv[0]}: Usage - {os.sys.argv[0]} <first_argument> <second_argument>")
    exit(1)

first_argument = os.sys.argv[1]
second_argument = os.sys.argv[2]


if len(first_argument) > 5 or len(second_argument) > 5:
    print(f"{os.sys.argv[0]}: Arguments must be at most 5 characters each")
    exit(1)
if not first_argument or not second_argument:
    print(f"{os.sys.argv[0]}: Arguments cannot be empty")
    exit(1)
if not first_argument.isalpha() or not second_argument.isalpha():
    print(f"{os.sys.argv[0]}: Invalid string arguments")
    exit(1)

try:
    with open("top-100k-password-list.txt", "r") as file:
        passwords = file.readlines()
except FileNotFoundError:
    print(f"{os.sys.argv[0]}: File not found - top-100k-password-list.txt")
    exit(1)
except Exception as e:
    print(f"{os.sys.argv[0]}: An error occurred while reading the file - {str(e)}")
    exit(1)

filtered_passwords = []
for password in passwords:
    password = password.strip()
    if password.startswith(first_argument) and password.endswith(second_argument):
        filtered_passwords.append(password)

if filtered_passwords:
    with open("passwords.txt", "w") as output_file:
        output_file.write("\n".join(filtered_passwords))
    print("Passwords found and saved in passwords.txt")
else:
    print(f"No passwords found starting with '{first_argument}' and ending with '{second_argument}'")
