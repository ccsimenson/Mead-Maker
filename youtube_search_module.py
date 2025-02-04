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
            return []
        
        videos = []
        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append({"title": title, "url": video_url})
        
        return videos
    
    except requests.exceptions.RequestException as e:
        return []

