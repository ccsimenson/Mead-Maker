import requests

# Replace with your own YouTube Data API key
YOUTUBE_API_KEY = "AIzaSyBBvVIzkFgrSaT_l4qTmRzODRGeFcA3llQ"

def search_youtube(query, max_results=5):
    """
    Search YouTube for videos based on a query.
    
    Parameters:
    query (str): The search term (e.g., "mead recipe").
    max_results (int): Maximum number of results to return.
    
    Returns:
    list: A list of video titles and URLs.
    """
    # YouTube Data API endpoint for search
    url = "https://www.googleapis.com/youtube/v3/search"
    
    # Parameters for the API request
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }
    
    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        # Extract video details
        videos = []
        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append({"title": title, "url": url})
        
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
    
    print(f"\nSearching YouTube for '{query}'...")
    videos = search_youtube(query)
    
    if videos:
        print("\n--- Search Results ---")
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video['title']}")
            print(f"   Link: {video['url']}")
    else:
        print("No results found. Please try a different search term.")

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
            abv_calculator()  # Assuming this function is already defined
        elif choice == "2":
            honey_water_calculator()  # Assuming this function is already defined
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