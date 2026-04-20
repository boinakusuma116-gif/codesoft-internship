import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_special=True):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Base characters (always included)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_chars = lower + upper + digits + special

    if not all_chars:
        raise ValueError("At least one character set must be selected")

    # Ensure at least one character from each selected type
    password = [
        random.choice(lower),
    ]

    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    # Fill remaining length
    remaining_length = length - len(password)
    password += [random.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)


def get_user_input():
    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length < 4:
                print("Length must be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_upper, use_digits, use_special


def main():
    print("=== Password Generator ===")
    
    length, use_upper, use_digits, use_special = get_user_input()
    
    password = generate_password(length, use_upper, use_digits, use_special)
    
    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
