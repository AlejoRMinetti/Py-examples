from pytube import YouTube
import os
from datetime import datetime

def download_videos(channel_id, date_from):
    youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        publishedAfter=date_from.isoformat()+"Z",
        type='video',
        maxResults=50
    )
    response = request.execute()
    for video in response['items']:
        yt = YouTube(f'https://www.youtube.com/watch?v={video["id"]["videoId"]}')
        stream = yt.streams.first()
        stream.download()
        print(f'Video {video["snippet"]["title"]} has been downloaded')
