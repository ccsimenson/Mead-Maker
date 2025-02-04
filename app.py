# Mead Making App - Main Menu

from tkinter import Tk, Button, Label, Frame, Entry, StringVar, OptionMenu, Listbox
from abv import calculate_abv  # Assuming your ABV function is in abv_module.py
from honey_ratio_module import calculate_honey_water_ratio  # Importing the honey-water ratio function
from youtube_search_module import search_youtube  # Importing the YouTube search function

def show_abv_page():
    main_menu_frame.pack_forget()
    abv_frame.pack(pady=20)

def show_recipe_page():
    pass  # Implement navigation to the recipe guide page

def show_ratio_page():
    main_menu_frame.pack_forget()
    ratio_frame.pack(pady=20)

def show_youtube_search_page():
    main_menu_frame.pack_forget()
    youtube_search_frame.pack(pady=20)

def show_main_menu():
    abv_frame.pack_forget()
    recipe_frame.pack_forget()
    ratio_frame.pack_forget()
    youtube_search_frame.pack_forget()
    main_menu_frame.pack(pady=20)

def get_abv():
    try:
        og = float(og_var.get())
        fg = float(fg_var.get())
        abv_result = calculate_abv(og, fg)
        result_var.set(f"ABV: {abv_result}%")
    except ValueError:
        result_var.set("Invalid input. Please enter numeric values.")

def get_honey_ratio():
    try:
        batch_size = float(batch_size_var.get())
        sweetness = sweetness_var.get()
        honey_amount, water_amount = calculate_honey_water_ratio(batch_size, sweetness)
        ratio_result_var.set(f"Honey: {honey_amount:.2f} L, Water: {water_amount:.2f} L")
    except ValueError:
        ratio_result_var.set("Invalid input. Please enter numeric values.")

def search_youtube_videos():
    query = youtube_query_var.get()
    if not query:
        youtube_result_var.set("Search term cannot be empty.")
        return
    
    videos = search_youtube(query)
    if videos:
        youtube_results_list.delete(0, 'end')
        for video in videos:
            youtube_results_list.insert('end', f"{video['title']} - {video['url']}")
    else:
        youtube_results_list.delete(0, 'end')
        youtube_result_var.set("No results found. Please try a different search term.")

# Initialize the GUI
root = Tk()
root.title("Mead Making App")

# Main menu frame
main_menu_frame = Frame(root)
Label(main_menu_frame, text="Mead Making App", font=('Helvetica', 16)).pack(pady=10)
Button(main_menu_frame, text="1. Calculate ABV", command=show_abv_page).pack(pady=5)
Button(main_menu_frame, text="2. Honey Ratio Calculator", command=show_ratio_page).pack(pady=5)
Button(main_menu_frame, text="3. Search YouTube for Mead Recipes", command=show_youtube_search_page).pack(pady=5)
Button(main_menu_frame, text="4. Exit", command=root.quit).pack(pady=5)

# ABV page frame
abv_frame = Frame(root)
Label(abv_frame, text="ABV Calculator", font=('Helvetica', 16)).pack(pady=10)
Label(abv_frame, text="Original Gravity (OG)").pack(pady=5)
og_var = StringVar()
Entry(abv_frame, textvariable=og_var).pack(pady=5)

Label(abv_frame, text="Final Gravity (FG)").pack(pady=5)
fg_var = StringVar()
Entry(abv_frame, textvariable=fg_var).pack(pady=5)

Button(abv_frame, text="Calculate ABV", command=get_abv).pack(pady=10)
result_var = StringVar()
Label(abv_frame, textvariable=result_var).pack(pady=5)
Button(abv_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# Honey ratio page frame
ratio_frame = Frame(root)
Label(ratio_frame, text="Honey-to-Water Ratio Calculator", font=('Helvetica', 16)).pack(pady=10)
Label(ratio_frame, text="Batch Size (liters)").pack(pady=5)
batch_size_var = StringVar()
Entry(ratio_frame, textvariable=batch_size_var).pack(pady=5)

Label(ratio_frame, text="Sweetness Level").pack(pady=5)
sweetness_var = StringVar(value="semi-sweet")
OptionMenu(ratio_frame, sweetness_var, "dry", "semi-sweet", "sweet").pack(pady=5)

Button(ratio_frame, text="Calculate Ratio", command=get_honey_ratio).pack(pady=10)
ratio_result_var = StringVar()
Label(ratio_frame, textvariable=ratio_result_var).pack(pady=5)
Button(ratio_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# YouTube search page frame
youtube_search_frame = Frame(root)
Label(youtube_search_frame, text="YouTube Mead Recipe Search", font=('Helvetica', 16)).pack(pady=10)
Label(youtube_search_frame, text="Search Term").pack(pady=5)
youtube_query_var = StringVar()
Entry(youtube_search_frame, textvariable=youtube_query_var).pack(pady=5)

Button(youtube_search_frame, text="Search", command=search_youtube_videos).pack(pady=10)
youtube_result_var = StringVar()
Label(youtube_search_frame, textvariable=youtube_result_var).pack(pady=5)
youtube_results_list = Listbox(youtube_search_frame, width=80)
youtube_results_list.pack(pady=5)
Button(youtube_search_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# Placeholder frame for recipe page
recipe_frame = Frame(root)

# Show the main menu on start
show_main_menu()

# Run the app
root.mainloop()
