from googleapiclient.discovery import build
from pytube import YouTube
import json

api_key = "AIzaSyD4fvKekZwAM4KuCeuRujQeYpkFVSyUku0"
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

video_ids = video_ids[:-31]

# for video in video_ids:
    # request = youtube.videos().list(
    #     part="snippet",
    #     id=video_ids[-1]
    # )

    # response = request.execute()
    # print(response)

# downloading video
yt = YouTube(youtube_video_url + video_ids[-1])
print("ADAPTIVE:\n\n\n")
for encoding in yt.streams.filter(adaptive=True):
    print(encoding)
print("PROGRESSIVE:\n\n\n")
for encoding in yt.streams.filter(progressive=True, file_extension='mp4'):
    print(encoding)


video_stream = yt.streams.filter(file_extension='mp4', adaptive=True).order_by('resolution').desc().first()
audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# Download video and audio files
video_file = video_stream.download(filename_prefix="video_")
audio_file = audio_stream.download(filename_prefix="audio_")

print("Video download completed:", video_file)
print("Audio download completed:", audio_file)

# # Serializing json
# json_object = json.dumps(response, indent=4)
 
# # Writing to sample.json
# with open("output.json", "w") as outfile:
#     outfile.write(json_object)