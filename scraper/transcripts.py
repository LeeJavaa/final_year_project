from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from pytube import YouTube
import json
import os
import pandas as pd
from dotenv import load_dotenv

# load_dotenv()

# # Building API Object
# api_key = os.getenv("API_KEY")
# channel_id = "UCm5mt-A4w61lknZ9lCsZtBw"
# api_service_name = "youtube"
# api_version = "v3"
# youtube_video_url = "http://youtube.com/watch?v="

# youtube = build(api_service_name, api_version, developerKey=api_key)

# # Getting Uploaded Videos Playlist
# request = youtube.channels().list(
#     part='contentDetails',
#     id=channel_id
# )

# response = request.execute()

# playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# # Getting all video IDs of channel
# next_page_token = None
# video_ids = []

# while True:
#     response = youtube.playlistItems().list(
#         part='contentDetails',
#         playlistId=playlist_id,
#         maxResults=50,
#         pageToken=next_page_token
#     ).execute()

#     for item in response['items']:
#         video_ids.append(item['contentDetails']['videoId'])

#     next_page_token = response.get('nextPageToken')
#     if not next_page_token:
#         break
# video_ids = video_ids[:-31]

# # init pandas df
# df = pd.DataFrame(columns=['id', 'transcript'])
# i = 0

# for video_id in video_ids:
#     i += 1
#     print(i)
#     try:
#         transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
#         transcript = ''.join(item['text'] for item in transcript_data)
#         df.loc[len(df.index)] = [video_id, transcript]
#     except:
#         print('No subtitles...')
#         df.loc[len(df.index)] = [video_id, 'Subtitles Disabled']

# df.to_csv("../data/dataset/transcripts.csv", header=True, index=False)

# data = pd.read_csv('../data/dataset/data.csv')
# transcripts = pd.read_csv('../data/dataset/transcripts.csv')
# df = data.merge(transcripts, on='id')
# df.to_csv("../data/dataset/data-with-transcripts.csv", header=True, index=False)