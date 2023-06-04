import os
from googleapiclient.discovery import build
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
import json

def authenticate():
    # Set up OAuth2 credentials
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', scopes)
    creds = flow.run_local_server(port=8080)

    # Save the credentials for subsequent use
    credentials_file = "credentials.json"
    with open(credentials_file, 'w') as f:
        json.dump(credentials_to_dict(creds), f)

    return creds

def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes
    }

def upload_video(video_path, title, description, tags=[]):
    # Load the saved credentials
    credentials_file = "credentials.json"
    with open(credentials_file, 'r') as f:
        creds_data = json.load(f)
    creds = credentials.Credentials.from_authorized_user_info(creds_data)

    # Create a YouTube Data API client
    youtube = build('youtube', 'v3', credentials=creds)

    # Create a request body for the video resource
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags
        },
        'status': {
            'privacyStatus': 'private'  # You can modify the privacy status if needed
        }
    }

    # Create a MediaFileUpload object
    media = MediaFileUpload(video_path)

    # Call the API's videos().insert method to upload the video
    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media
    ).execute()

    # Print the video ID of the uploaded video
    print('Video uploaded successfully. Video ID:', response['id'])

# Authenticate and obtain credentials
credentials = authenticate()

# Call the upload_video function with the required parameters
video_path = './videos/oui.mp4'  # Replace with the actual path to your video file
title = 'My Uploaded Video'
description = 'Description of my video'
tags = ['tag1', 'tag2', 'tag3']  # Add tags if desired

upload_video(video_path, title, description, tags)
