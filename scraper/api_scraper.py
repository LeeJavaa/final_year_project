from googleapiclient.discovery import build
from pytube import YouTube
import json
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Building API Object
api_key = os.getenv("API_KEY")
channel_id = "UCm5mt-A4w61lknZ9lCsZtBw"
api_service_name = "youtube"
api_version = "v3"
youtube_video_url = "http://youtube.com/watch?v="

youtube = build(api_service_name, api_version, developerKey=api_key)

# Getting Uploaded Videos Playlist
request = youtube.channels().list(
    part='contentDetails',
    id=channel_id
)

response = request.execute()

playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Getting all video IDs of channel
next_page_token = None
video_ids = []

while True:
    response = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

# Split all video IDs into batches of 50, then fetch API data for each video in batch. Thus getting API data for all videos.
video_ids = video_ids[:-31]
for i in range(0, len(video_ids), 50):
    batch = video_ids[i:i+50]
    batch_string = ','.join(batch)
    response = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=batch_string,
            fields = 'items(id,snippet(publishedAt, title, description),contentDetails.duration, statistics(viewCount, likeCount, commentCount))',
            maxResults=50,
            pageToken=next_page_token
        ).execute()
    json_object = json.dumps(response, indent=4)
    dict = json.loads(json_object)
    df = pd.json_normalize(dict['items'])
    if os.path.exists("../data/dataset/raw_data.csv"):
        df.to_csv("../data/dataset/raw_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("../data/dataset/raw_data.csv", header=True, index=False)