from googleapiclient.discovery import build
from datetime import datetime, timedelta

youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')

# Get the list of subscribed channels
request = youtube.subscriptions().list(
    part='snippet',
    mine=True,
    maxResults=50
)
response = request.execute()

# Get the last 30 days videos
thirty_days_ago = datetime.now() - timedelta(days=30)

for item in response['items']:
    channel_id = item['snippet']['resourceId']['channelId']
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        publishedAfter=thirty_days_ago.isoformat()+"Z",
        type='video',
        maxResults=50
    )
    response = request.execute()
    for video in response['items']:
        print(video['snippet']['title'], video['snippet']['channelTitle'])



# check if watched
request = youtube.videos().list(
    part='statistics',
    id='YOUR_VIDEO_ID'
)
response = request.execute()

if int(response['items'][0]['statistics']['viewCount']) > 0:
    print('Video has been watched')
else:
    print('Video has not been watched')

# delete this video
youtube.playlistItems().delete(id='YOUR_VIDEO_ID').execute()