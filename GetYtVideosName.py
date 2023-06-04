from googleapiclient.discovery import build

# Set up the API key
api_key = 'AIzaSyBkmOuQYBLVHHlFlnmzfxgEYqYu0ZhspIk'

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_url):
    # Extract the channel ID from the channel URL
    channel_id = channel_url.split('/')[-1]

    # Retrieve the playlist ID of the channel's uploaded videos
    channel_response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    if not channel_response['items']:
        print('Invalid YouTube channel URL')
        return

    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve the videos in the channel's uploads playlist
    videos_response = youtube.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=50
    ).execute()

    videos = videos_response['items']
    if videos:
        for video in videos:
            video_title = video['snippet']['title']
            video_id = video['snippet']['resourceId']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'

            # Retrieve the duration of the video using contentDetails API
            video_response = youtube.videos().list(
                part='contentDetails',
                id=video_id
            ).execute()

            duration = video_response['items'][0]['contentDetails']['duration']
            
            print(f'Title: {video_title}')
            print(f'URL: {video_url}')
            print(f'Duration: {duration}')
            print('---')
    else:
        print('No videos found in the channel playlist.')

# Prompt the user for a YouTube channel URL
channel_url = input('Enter a YouTube channel URL: ')

# Call the function to fetch and display the video information
get_channel_videos(channel_url)
