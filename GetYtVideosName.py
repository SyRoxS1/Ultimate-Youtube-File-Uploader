from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set your API key or OAuth 2.0 client credentials
API_KEY = 'AIzaSyBkmOuQYBLVHHlFlnmzfxgEYqYu0ZhspIk'  # Replace with your API key or set up OAuth 2.0

# Create a YouTube Data API service
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_names(channel_url):
    try:
        # Extract channel ID from the URL
        channel_id = channel_url.split('/')[-1]

        # Retrieve the channel's uploads playlist ID
        channels_response = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        ).execute()

        uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Retrieve the videos in the uploads playlist
        playlist_items = []
        next_page_token = None

        while True:
            playlist_response = youtube.playlistItems().list(
                part='snippet',
                playlistId=uploads_playlist_id,
                maxResults=50,  # Adjust as per your requirement
                pageToken=next_page_token
            ).execute()

            playlist_items.extend(playlist_response['items'])
            next_page_token = playlist_response.get('nextPageToken')

            if not next_page_token:
                break

        # Extract video names
        video_names = [item['snippet']['title'] for item in playlist_items]
        return video_names

    except HttpError as e:
        print(f'An HTTP error occurred:\n{e}')

# Example usage
channel_url = 'https://www.youtube.com/channel/UCyj7svz9hL15ciYwrV_wpLg'
video_names = get_video_names(channel_url)
for name in video_names:
    print(name)
