from tkinter import Tk, Button, Label, Frame, Entry, StringVar, Listbox, Scrollbar, messagebox
import webbrowser
import threading
from googleapiclient.discovery import build


# Initialize Tkinter root
root = Tk()

API_KEY = "AIzaSyBBvVIzkFgrSaT_l4qTmRzODRGeFcA3llQ"

youtube = build("youtube", "v3", developerKey=API_KEY)


# Main menu frame
main_menu_frame = Frame(root)
Label(main_menu_frame, text="Main Menu", font=('Norse', 16)).pack(pady=10)
Button(main_menu_frame, text="Go to YouTube Search", command=lambda: youtube_search_frame.pack(pady=20)).pack(pady=5)

# YouTube API Setup (Add your API key here)
youtube = build("youtube", "v3", developerKey=API_KEY)

def search_youtube_videos(query_var, results_list, status_label, next_page_token=None):
    try:
        query = query_var.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search term")
            return

        status_label.config(text="Searching...", fg="blue")
        
        # API request
        threading.Thread(target=execute_search, args=(query, results_list, status_label, next_page_token)).start()
        
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
        
# Execute in thread to prevent GUI freeze
def execute_search(request, results_list):
    try:
        response = request.execute()
        videos = []
        for item in response['items']:
            video_id = item['id']['videoId']
def execute_search(query, results_list, status_label, next_page_token):
    try:
        request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=10,
            pageToken=next_page_token or ""
        )
            videos.append((video_id, title))
                
            results_list.delete(0, 'end')
            for video in videos:
                results_list.insert('end', video[1])
                
            status_label.config(text=f"Found {len(videos)} results", fg="green")
                
            # Enable/disable pagination buttons
            prev_btn = youtube_search_frame.nametowidget('prev_btn')
            next_btn = youtube_search_frame.nametowidget('next_btn')
            prev_btn['state'] = 'normal' if response.get('prevPageToken') else 'disabled'
            next_btn['state'] = 'normal' if response.get('nextPageToken') else 'disabled'
                
            # Store page tokens
            youtube_search_frame.prev_page_token = response.get('prevPageToken')
            youtube_search_frame.next_page_token = response.get('nextPageToken')
                
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
        
    threading.Thread(target=execute_search).start()

def open_video(results_list):
    selection = results_list.curselection()
    if selection:
        index = selection[0]
        video_id = results_list.get(index).split("|")[0].strip()
        webbrowser.open(f"https://youtube.com/watch?v={video_id}")

# Function to show the main menu
def show_main_menu():
    youtube_search_frame.pack_forget()
    main_menu_frame.pack(pady=20)
    pass


# In your YouTube search frame setup:
youtube_search_frame = Frame(root)
Label(youtube_search_frame, text="YouTube Mead Recipe Search", font=('Norse', 16)).pack(pady=10)

# Search box
search_frame = Frame(youtube_search_frame)
search_frame.pack(pady=5)
Label(search_frame, text="Search Term:").pack(side='left')
youtube_query_var = StringVar()
Entry(search_frame, textvariable=youtube_query_var, width=40).pack(side='left', padx=5)

# Status label
status_label = Label(youtube_search_frame, text="", fg="black")
status_label.pack()

# Results list with scrollbar
results_frame = Frame(youtube_search_frame)
results_frame.pack(pady=5)

scrollbar = Scrollbar(results_frame)
scrollbar.pack(side='right', fill='y')

youtube_results_list = Listbox(results_frame, width=80, height=15, yscrollcommand=scrollbar.set)
youtube_results_list.pack(side='left')
youtube_results_list.bind('<Double-1>', lambda e: open_video(e, youtube_results_list))
scrollbar.config(command=youtube_results_list.yview)

# Pagination controls
pagination_frame = Frame(youtube_search_frame)
pagination_frame.pack(pady=5)

Button(pagination_frame, text="Previous", name='prev_btn', 
       command=lambda: search_youtube_videos(youtube_query_var, youtube_results_list, status_label, 
                                            youtube_search_frame.prev_page_token)).pack(side='left', padx=5)

Button(pagination_frame, text="Next", name='next_btn',
       command=lambda: search_youtube_videos(youtube_query_var, youtube_results_list, status_label,
                                           youtube_search_frame.next_page_token)).pack(side='left', padx=5)

# Search button
Button(youtube_search_frame, text="Search", 
       command=lambda: search_youtube_videos(youtube_query_var, youtube_results_list, status_label)).pack(pady=5)



# Back button
Button(youtube_search_frame, text="Back to Main Menu", command=show_main_menu).pack(pady=10)

