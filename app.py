# Mead Making App - Main Menu


import abv
import honey_ratio
import mead_recipe

def main_menu():
    """
    Display the main menu of the mead-making app.
    """
    while True:
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            abv()
        elif choice == "2":
            print("\n--- Mead Recipe Guide ---")
            mead_recipe()
        elif choice == "3":
            honey_ratio()
        elif choice == "4":    
            print("Exiting the app. Happy brewing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the app
if __name__ == "__main__":
    main_menu()