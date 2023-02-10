from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')

request = youtube.playlistItems().list(
    part='snippet',
    playlistId='YOUR_PLAYLIST_ID',
    maxResults=50
)
response = request.execute()

for item in response['items']:
    print(item['snippet']['title'])
