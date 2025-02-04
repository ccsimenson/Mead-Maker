# Formula for determining alcohol by volume percent
# ABV = (Original Gravity (OG) - Final Gravity (FG)) * 131.25

# Function to calculate ABV
def calculate_abv(og, fg):
    """
    Calculate Alcohol By Volume (ABV) percentage.

    Parameters:
    og (float): Original Gravity reading.
    fg (float): Final Gravity reading.

    Returns:
    float: ABV percentage rounded to 2 decimal places.
    """
    abv = (og - fg) * 131.25
    return round(abv, 2)

def get_abv():
    """
    Prompt user for Original Gravity (OG) and Final Gravity (FG) readings,
    calculate the ABV, and print the result.
    """
    try:
        ogr = float(input("Original Gravity Reading: "))
        fgr = float(input("Enter Final Gravity Reading: "))
        abv_result = calculate_abv(ogr, fgr)
        print(f"ABV: {abv_result}%")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# To integrate this into your main menu app:
def main_menu():
    """
    Display the main menu of the mead-making app.
    """
    while True:
        print("\n--- Mead Master Main Menu ---")
        print("1. Calculate ABV (Alcohol by Volume)")
        print("2. View Mead Recipe Guide")
        print("3. Calculate Honey to Water Ratio")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            get_abv()
        elif choice == "2":
            print("\n--- Mead Recipe Guide ---")
            mead_recipe.view_guide()  # Ensure this function is defined in mead_recipe.py
        elif choice == "3":
            honey_ratio.calculate_ratio()  # Ensure this function is defined in honey_ratio.py
        elif choice == "4":    
            print("Exiting the app. Happy brewing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the app
if __name__ == "__main__":
    main_menu()
