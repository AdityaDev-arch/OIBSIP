#Imported string to get character sets and random for random selection
import string
import random

# Helper function to handle y/n questions
def get_boolean_input(prompt):
    while True:
        choice = input(prompt).lower().strip() # .strip() handles accidental spaces
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Oops! Please just type 'y' or 'n'.")

def generate_password():
    print("-" * 50)
    print("Welcome to my Random Password Generator!")
    print("-" * 50)

    try:
        # Get length and make sure it's valid
        length = int(input("How long should the password be? "))
        if length <= 0:
            print("The length has to be at least 1!")
            return
        
        # Gathering user preferences
        use_letters = get_boolean_input("Include letters? (y/n): ")
        use_numbers = get_boolean_input("Include numbers? (y/n): ")
        use_symbols = get_boolean_input("Include symbols? (y/n): ")

        # Combine the character sets based on the choices above
        char_pool = ""
        if use_letters:
            char_pool += string.ascii_letters
        if use_numbers:
            char_pool += string.digits
        if use_symbols:
            char_pool += string.punctuation

        # Safety check: what if they said 'n' to everything?
        if not char_pool:
            print("Error: You need to pick at least one character type to make a password!")
            return

        # Pick random characters and join them into a string
        password = "".join(random.choice(char_pool) for _ in range(length))

        print("\n" + "=" * 50)
        print(f"DONE! Your new password is: {password}")
        print("=" * 50)

    except ValueError:
        print("That's not a valid number! Please enter digits for the length.")

if __name__ == "__main__":
    generate_password()