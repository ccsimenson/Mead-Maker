import requests
import os

# YouTube Data API key from environment variable
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "AIzaSyBBvVIzkFgrSaT_l4qTmRzODRGeFcA3llQ")

def search_youtube(query, max_results=5):
    """
    Search YouTube for videos based on a query.
    
    Parameters:
    query (str): The search term (e.g., "mead recipe").
    max_results (int): Maximum number of results to return.
    
    Returns:
    list: A list of video titles and URLs.
    """
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "error" in data:
            error_message = data["error"].get("message", "Unknown error occurred.")
            print(f"YouTube API Error: {error_message}")
            return []
        
        videos = []
        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append({"title": title, "url": video_url})
        
        return videos
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from YouTube API: {e}")
        return []

def youtube_search_feature():
    """
    Guide the user through searching for mead recipes on YouTube.
    """
    print("\n--- YouTube Mead Recipe Search ---")
    query = input("Enter a search term (e.g., 'mead recipe'): ")
    
    if not query:
        print("Search term cannot be empty. Please try again.")
        return
    
    print(f"\nSearching YouTube for '{query}'...")
    videos = search_youtube(query)
    
    if videos:
        print("\n--- Search Results ---")
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video['title']}")
            print(f"   Link: {video['url']}")
    else:
        print("No results found. Please try a different search term.")

def abv_calculator():
    """
    Prompt user for Original Gravity (OG) and Final Gravity (FG) readings,
    calculate the ABV, and print the result.
    """
    def calculate_abv(og, fg):
        abv = (og - fg) * 131.25
        return round(abv, 2)

    try:
        ogr = float(input("Original Gravity Reading: "))
        fgr = float(input("Enter Final Gravity Reading: "))
        abv_result = calculate_abv(ogr, fgr)
        print(f"ABV: {abv_result}%")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def honey_water_calculator():
    """
    Placeholder function for Honey-to-Water Ratio Calculator.
    """
    print("Honey-to-Water Ratio Calculator coming soon...")

def main_menu():
    """
    Display the main menu of the mead-making app.
    """
    while True:
        print("\n=== Mead Making App ===")
        print("1. Calculate ABV")
        print("2. Honey-to-Water Ratio Calculator")
        print("3. Search YouTube for Mead Recipes")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            abv_calculator()
        elif choice == "2":
            honey_water_calculator()
        elif choice == "3":
            youtube_search_feature()
        elif choice == "4":
            print("Exiting the app. Happy brewing!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the app
if __name__ == "__main__":
    main_menu()
