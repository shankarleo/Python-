import random
import string

def gen_pass():
    length = int(input("Enter Password Length: ").strip())
    Uppercase = input("Include Uppercase letters (yes/no): ").strip().lower()
    Special = input("Include Special characters (yes/no): ").strip().lower()
    Digits = input("Include Digits (yes/no): ").strip().lower()

    if length < 4:
        print("Password cannot be generated")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if Uppercase == "yes" else ""
    special = "!@#$%^&*()" if Special == "yes" else ""
    digits = string.digits if Digits == "yes" else ""

    Total = lower + uppercase + special + digits

    required_char = []

    if Uppercase == "yes":
        required_char.append(random.choice(uppercase))
    if Special == "yes":
        required_char.append(random.choice(special))
    if Digits == "yes":
        required_char.append(random.choice(digits))

    remaining = length - len(required_char)
    password = required_char.copy()

    for _ in range(remaining):
        password.append(random.choice(Total))

    random.shuffle(password)

    return "".join(password)


password = gen_pass()
print("Generated Password:", password)