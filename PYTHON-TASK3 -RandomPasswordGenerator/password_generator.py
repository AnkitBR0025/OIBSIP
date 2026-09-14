# Name:- Ankit Kumar Pandey
# Track:- python Programming
# Task Title:- Random Password Generator






import random
import string



def main():
    print("\n-----RANDOM PASSWORD GENERATOR-----\n")
    

    while True:
        length = get_password_length()
        pool, required_categories = get_character_pool()

        password = generate_password(length, pool, required_categories)

        print("\n" + "-" * 35)
        print("Generated Password: " + password)
        print("-" * 35 + "\n")

        again = input("Do you want to generate another password? (y/n): ").strip().lower()
        if again !="y":
            print("\nThanks for using the Password Generator. Goodbye!")
            break
        print("\n" + "=" * 35)




def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length >= 8:
                return length
            print("Length must be at least 8 characters. Try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")


def get_character_pool():
    while True:
        print("\nSelect character types to include (y/n):")
        print("(select at least 2 character types)")
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
        use_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

        selected_types = []
        character_pool = ""

        if use_upper:
            selected_types.append(string.ascii_uppercase)
            character_pool += string.ascii_uppercase
        if use_lower:
            selected_types.append(string.ascii_lowercase)
            character_pool += string.ascii_lowercase
        if use_digits:
            selected_types.append(string.digits)
            character_pool += string.digits
        if use_symbols:
            selected_types.append(string.punctuation)
            character_pool += string.punctuation

        if len(selected_types) >= 2:
            return character_pool,selected_types
        
        print("\n[!] You must select at least 2 character types. Let's try again.")

def generate_password(length, pool, required_categories):
    password = []


    for category in required_categories:
        char = random.choice(category)
        password.append(char)

    
    remaining = length - len(password)
    for i in range(remaining):
        char = random.choice(pool)
        password.append(char)


    random.shuffle(password)
    return "".join(password)



if __name__ == "__main__":
    main()