from abv import calculate_abv  # Assuming your ABV function is in abv_module.py
from honey_ratio_module import calculate_honey_water_ratio  # Importing the honey-water ratio function
from youtube_search_module import search_youtube_videos# Importing the YouTube search function


#Function to calculate ABV
def get_abv(result_var, og, fg, abv_result):
    try:
        og = float(og.get())
        fg = float(fg.get())
        abv_result = calculate_abv(og, fg)
        result_var.set(f"ABV: {abv_result}%")
    except ValueError:
        result_var.set("Invalid input. Please enter numeric values.")
    pass


#Function to calculate honey-water ratio
def get_honey_ratio(batch_size, sweetness, honey_amount, water_amount, ratio_result_var):
    try:
        batch_size = float(batch_size.get())
        sweetness = sweetness.get()
        honey_amount, water_amount = calculate_honey_water_ratio(batch_size, sweetness)
        ratio_result_var.set(f"Honey: {honey_amount:.2f} L, Water: {water_amount:.2f} L")
    except ValueError:
        ratio_result_var.set("Invalid input. Please enter numeric values.")
    pass

#Function to search YouTube videos
def search_youtube_videos(query_var, results_list, results_var):
    query_var = query_var.get()
    if not query_var:
        results_var.set("Search term cannot be empty.")
        return
    
    videos = search_youtube(query_var,results_var)
    if videos:
        results_list.delete(0, 'end')
        for video in videos:
            results_list.insert('end', f"{video['title']} - {video['url']}")
    else:
        results_list.delete(0, 'end')
        results_var.set("No results found. Please try a different search term.")
    pass
