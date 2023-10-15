import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Create a pool of characters based on user preferences
    character_pool = []
    character_pool.extend(lowercase_letters)
    character_pool.extend(uppercase_letters)
    character_pool.extend(digits)
    character_pool.extend(special_characters)

    # Ensure the password length is at least 6 characters
    if length < 6:
        print("Password length must be at least 6 characters.")
        return None

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            password = generate_password(length)
            if password:
                print("Generated Password: ", password)
                break
        except ValueError:
            print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
