"""Simple menu-driven program"""

def display_menu():
    """Shows menu options"""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def handle_menu_choice(choice):
    """Processes user's choice"""
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice.")
    return False

def greet_user():
    """Prints a greeting"""
    print("Hello! Welcome!\n")

def even_odd_checker():
    """Checks if a number is even or odd"""
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an Even number.\n")
    else:
        print(f"{num} is an Odd number.\n")

if __name__ == "__main__":
    while True:
        display_menu()
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(user_choice):
                break
        except ValueError:
            print("Invalid input.")
