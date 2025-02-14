from googleapiclient.discovery import build
import googleapiclient.errors
import re


def get_channel_videos(channel_url):
    # Set up the API key
    api_key = 'AIzaSyBkmOuQYBLVHHlFlnmzfxgEYqYu0ZhspIk'

    # Create a YouTube Data API client
    youtube = build('youtube', 'v3', developerKey=api_key)
    # Extract the channel ID from the channel URL
    channel_id = channel_url.split('/')[-1]

    print(channel_id)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forHandle="@sysyrocks"
    )
    response = request.execute()


    print(response)
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
    vidcount = 1
    urls = {}
    if videos:
        for video in videos:
            video_title = video['snippet']['title']
            video_id = video['snippet']['resourceId']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'

            # Retrieve the duration of the video using contentDetails API
            video_duration_response = youtube.videos().list(
                part='contentDetails',
                id=video_id
            ).execute()
            

            
            duration = video_duration_response['items'][0]['contentDetails']['duration']
            description = video['snippet']['description']
            duration = re.findall('\d+',duration)
            if len(duration) == 1:
                temps = ('Duration:',duration[0],'sec')
                urls.update({str(vidcount): [video_url,video_title,temps,description] })
            else:
                temps = ('Duration:',duration[0],'min',duration[1],'sec')
                urls.update({str(vidcount): [video_url,video_title,temps,description] })
            vidcount += 1
            
            
    else:
        print('No videos found in the channel playlist.')

    return urls


