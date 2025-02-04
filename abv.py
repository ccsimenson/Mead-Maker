# Formula for determining alcohol by volume percent
# ABV = (Original Gravity (OG) - Final Gravity (FG)) * 131.25


try:
    ogr = float(input("Original Gravity Reading: "))
    fgr = float(input("Enter Final Gravity Reading: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()


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
    abv = (og - fg) * 131.25
    return round(abv, 2)  # Round to 2 decimal places for readability

# Calculate and print ABV
abv_result = calculate_abv(ogr, fgr)
print(f"ABV: {abv_result}%")