import string
import secrets

def generate_random_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "No character types selected for the password."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random Password Generator")

    password_length = int(input("Enter the desired password length: "))
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_random_password(password_length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    print("Generated Password:", password)
