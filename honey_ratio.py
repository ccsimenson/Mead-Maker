def get_batch_size():
    """
    Prompt the user for the desired batch size and validate the input.
    
    Returns:
    float: The batch size in liters.
    """
    while True:
        try:
            batch_size = float(input("Enter the desired batch size (in liters): "))
            if batch_size <= 0:
                print("Batch size must be a positive number. Please try again.")
            else:
                return batch_size
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_sweetness_level():
    """
    Prompt the user for the desired sweetness level and validate the input.
    
    Returns:
    str: The sweetness level (dry, semi-sweet, sweet).
    """
    while True:
        sweetness = input("Enter the desired sweetness level (dry, semi-sweet, sweet): ").strip().lower()
        if sweetness in ["dry", "semi-sweet", "sweet"]:
            return sweetness
        else:
            print("Invalid input. Please choose from 'dry', 'semi-sweet', or 'sweet'.")

def calculate_honey_water_ratio(batch_size, sweetness):
    """
    Calculate the required amount of honey and water based on batch size and sweetness level.
    
    Parameters:
    batch_size (float): The desired batch size in liters.
    sweetness (str): The desired sweetness level.
    
    Returns:
    tuple: A tuple containing (honey_amount, water_amount) in liters.
    """
    # Define honey-to-water ratios based on sweetness level
    ratios = {
        "dry": 0.15,       # 15% honey, 85% water
        "semi-sweet": 0.25, # 25% honey, 75% water
        "sweet": 0.35       # 35% honey, 65% water
    }
    
    honey_ratio = ratios.get(sweetness, 0.25)  # Default to semi-sweet if invalid sweetness
    honey_amount = batch_size * honey_ratio
    water_amount = batch_size - honey_amount
    
    return honey_amount, water_amount

def honey_water_calculator():
    """
    Guide the user through the honey-to-water ratio calculation process.
    """
    print("\n--- Honey-to-Water Ratio Calculator ---")
    batch_size = get_batch_size()
    sweetness = get_sweetness_level()
    
    honey_amount, water_amount = calculate_honey_water_ratio(batch_size, sweetness)
    
    print("\n--- Results ---")
    print(f"Batch Size: {batch_size} liters")
    print(f"Sweetness Level: {sweetness}")
    print(f"Honey Required: {honey_amount:.2f} liters")
    print(f"Water Required: {water_amount:.2f} liters")

#def main_menu():
#   """
# 
#   Display the main menu of the mead-making app.
#   """
#   while True:
#       print("\n=== Mead Making App ===")
#       print("1. Calculate ABV")
#       print("2. Honey-to-Water Ratio Calculator")
#       print("3. Mead Recipe Guide")
#       print("4. Exit")
#       
#       choice = input("Select an option (1-4): ")
        
#       if choice == "1":
#           abv_calculator()  # Assuming this function is already defined
#       elif choice == "2":
#           honey_water_calculator()
#       elif choice == "3":
#           print("\n--- Mead Recipe Guide ---")
#           print("This feature is under development. Stay tuned!")
#       elif choice == "4":
#           print("Exiting the app. Happy brewing!")
#           break
#       else:
#           print("Invalid choice. Please select a valid option.")

# Run the app
# if __name__ == "__main__":
#   main_menu()