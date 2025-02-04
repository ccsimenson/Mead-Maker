# Mead Making App - Main Menu


import abv
import honey_ratio
import mead_recipes

def main_menu():
    """
    Display the main menu of the mead-making app.
    """
    while True:
        print("\n=== Mead Making App ===")
        print("1. Calculate ABV")
        print("2. Mead Recipe Guide")
        print("3. Honey to Water Ratio")
        
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            command=abv
        elif choice == "2":
            print("\n--- Mead Recipe Guide ---")
            command=mead_recipes
        elif choice == "3":
            command=honey_ratio
        elif choice == "4":    
            print("Exiting the app. Happy brewing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the app
if __name__ == "__main__":
    main_menu()