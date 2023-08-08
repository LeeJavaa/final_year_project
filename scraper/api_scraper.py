from googleapiclient.discovery import build
from pytube import YouTube
import json
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
channel_id = "UCm5mt-A4w61lknZ9lCsZtBw"
api_service_name = "youtube"
api_version = "v3"
youtube_video_url = "http://youtube.com/watch?v="

youtube = build(api_service_name, api_version, developerKey=api_key)

# request = youtube.videos().list(
#     part="snippet, contentDetails, status, player, topicDetails, statistics, id",
#     id="nl9TZanwbBk"
# )

request = youtube.channels().list(
    part='contentDetails',
    id=channel_id
)

response = request.execute()

playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

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

# video_ids = video_ids[:-31]
video_ids = video_ids[:200]


video_ids_string = ','.join(video_ids)

request = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id=video_ids_string,
    fields = 'items(id,snippet(publishedAt, title, description),contentDetails.duration, statistics(viewCount, likeCount, commentCount))'
)
response = request.execute()

# Serializing json
json_object = json.dumps(response, indent=4)
dict = json.loads(json_object)
df = pd.json_normalize(dict['items'])
df.to_csv("../data/dataset/api_data.csv")
 
# Writing to sample.json
# with open("output.json", "w") as outfile:
#     outfile.write(json_object)