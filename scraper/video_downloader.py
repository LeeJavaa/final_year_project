import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from pytube import YouTube

# Import environment variables
load_dotenv()

# API variables
api_key = os.getenv("API_KEY")
channel_id = "UCm5mt-A4w61lknZ9lCsZtBw"
api_service_name = "youtube"
api_version = "v3"

# General variables
youtube_video_url = "http://youtube.com/watch?v="
cut_videos = 31 # Number of initial videos on steve brunton's channel that can be ignored

# Build the youtube api interface
youtube = build(api_service_name, api_version, developerKey=api_key)

# Get the 'uploaded videos' playlist
content = youtube.channels().list(
    part='contentDetails',
    id=channel_id
).execute()
playlist_id = content['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Fetch the ids of all videos uploaded
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

video_ids = video_ids[317:-cut_videos]
# print(video_ids)

# Checking streams
# yt = YouTube(youtube_video_url + video_ids[0])
# print("ADAPTIVE:\n\n\n")
# for encoding in yt.streams.filter(adaptive=True):
#     print(encoding)
# print("PROGRESSIVE:\n\n\n")
# for encoding in yt.streams.filter(progressive=True, file_extension='mp4'):
#     print(encoding)

# downloading videos (PROGRESSIVE ON, ADAPTIVE OFF)
for video_id in video_ids:
    yt = YouTube(youtube_video_url + video_id)
    video_stream = yt.streams.filter(file_extension='mp4', progressive=True, res="720p").order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(file_extension='mp4', only_audio=True).order_by('abr').desc().first()
    filename = video_id + ".mp4"
    video_file = video_stream.download(output_path="../data/video/", filename=filename)
    audio_file = audio_stream.download(output_path="../data/audio/", filename=filename)
    print("Video download completed:", video_file)
    print("Audio download completed:", audio_file)

# For only 1080p / 360p videos:
# yt = YouTube(youtube_video_url + video_ids[0])
# video_stream = yt.streams.filter(file_extension='mp4', adaptive=True, res="360p").order_by('resolution').desc().first()
# audio_stream = yt.streams.filter(file_extension='mp4', only_audio=True).order_by('abr').desc().first()
# filename = video_ids[0] + ".mp4"
# video_file = video_stream.download(output_path="../data/video/", filename=filename)
# audio_file = audio_stream.download(output_path="../data/audio/", filename=filename)
# print("Video download completed:", video_file)
# print("Audio download completed:", audio_file)