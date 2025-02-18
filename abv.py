# Formula for determining alcohol by volume percent
# ABV = (Original Gravity (OG) - Final Gravity (FG)) * 131.25

from tkinter import Tk, Label, Entry, Button, StringVar

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
    Get OG and FG readings from the user, calculate the ABV, and display the result.
    """
    try:
        og = float(og_var.get())
        fg = float(fg_var.get())
        abv_result = calculate_abv(og, fg)
        result_var.set(f"ABV: {abv_result}%")
    except ValueError:
        result_var.set("Invalid input. Please enter numeric values.")

# Initialize the GUI
root = Tk()
root.title("ABV Calculator")

# Original Gravity input
Label(root, text="Original Gravity (OG)").pack(pady=5)
og_var = StringVar()
Entry(root, textvariable=og_var).pack(pady=5)

# Final Gravity input
Label(root, text="Final Gravity (FG)").pack(pady=5)
fg_var = StringVar()
Entry(root, textvariable=fg_var).pack(pady=5)

# Calculate button
Button(root, text="Calculate ABV", command=get_abv).pack(pady=10)

# Result display
result_var = StringVar()
Label(root, textvariable=result_var).pack(pady=5)

# Run the app
root.mainloop()
