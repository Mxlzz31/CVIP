import random
import string

# generate password function 


def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        print("Error: At least one character type should be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# main function 


def main():
    print("Random Password Generator")

    length = int(input("Enter the password length: "))
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)

    if password:
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()
