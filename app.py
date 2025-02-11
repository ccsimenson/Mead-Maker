from tkinter import Tk, Button, Label, Frame, Entry, StringVar, OptionMenu, Listbox
from appfeatures import get_abv, get_honey_ratio, search_youtube_videos
# Initialize the GUI
root = Tk()
root.title("Mead Making App")

def show_abv_page():
    main_menu_frame.pack_forget()
    abv_frame.pack(pady=20)

def show_recipe_page():
    main_menu_frame.pack_forget()
    recipe_frame.pack(pady=20)

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

# Main menu frame
main_menu_frame = Frame(root)
Label(main_menu_frame, text="Mead Making App", font=('Norse', 16)).pack(pady=10)
Button(main_menu_frame, text="1. Calculate ABV", command=show_abv_page).pack(pady=5)
Button(main_menu_frame, text="2. Honey Ratio Calculator", command=show_ratio_page).pack(pady=5)
Button(main_menu_frame, text="3. Search YouTube for Mead Recipes", command=show_youtube_search_page).pack(pady=5)
Button(main_menu_frame, text="4. Exit", font='Norse', command=root.quit).pack(pady=5)

# ABV Calculator Frame
abv_frame = Frame(root)
Label(abv_frame, text="ABV Calculator", font=('Norse', 16)).pack(pady=10)
Button(abv_frame, text="Calculate ABV", command=get_abv).pack(pady=10)
result_var = StringVar()
Label(abv_frame, textvariable=result_var).pack(pady=5)
Button(abv_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# Honey Ratio Frame
ratio_frame = Frame(root)
Label(ratio_frame, text="Honey=Water Ratio Calculator", font=('Norse', 16)).pack(pady=10)
Button(ratio_frame, text="Calculate Ratio", command=get_honey_ratio).pack(pady=10)
Button(ratio_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# YouTube search page frame
youtube_search_frame = Frame(root)
Label(youtube_search_frame, text="YouTube Mead Recipe Search", font=('Norse', 16)).pack(pady=10)
Label(youtube_search_frame, text="Search Term").pack(pady=5)

Button(youtube_search_frame, text="Search", command=lambda: search_youtube_videos(youtube_query_var, youtube_results_list)).pack(pady=10)
youtube_results_list = Listbox(youtube_search_frame, width=80, height=15)
youtube_results_list.pack(pady=5)
Button(youtube_search_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# Recipe Guide Frame (placeholder)
recipe_frame = Frame(root)
Label(recipe_frame, text="Mead Recipe Guide (Coming Soon!)", font=('Norse', 16)).pack(pady=20)
Button(recipe_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

# Initialize the app with the main menu
show_main_menu()
root.mainloop()