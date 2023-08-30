import pandas as pd
import shutil
# from sklearn.model_selection import train_test_split

# df = pd.read_csv('../data/dataset/data-with-transcripts.csv')

# train_df, temp_df = train_test_split(df, test_size=0.2, random_state=42)
# val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# print(len(train_df.index))
# print(len(val_df.index))
# print(len(test_df.index))

# train_df.to_csv("../data/dataset/train/train.csv", header=True, index=False)
# val_df.to_csv("../data/dataset/validation/validation.csv", header=True, index=False)
# test_df.to_csv("../data/dataset/test/test.csv", header=True, index=False)

train_df = pd.read_csv("../data/dataset/train/train.csv")
val_df = pd.read_csv("../data/dataset/validation/validation.csv")
test_df = pd.read_csv("../data/dataset/test/test.csv")

train_ids = train_df['id'].values.tolist()
val_ids = val_df['id'].values.tolist()
test_ids = test_df['id'].values.tolist()

print(train_ids)
print(val_ids)
print(test_ids)

source_video_folder = "../data/video"
source_audio_folder = "../data/audio"
destination_video_folder_train = "../data/video/train"
destination_audio_folder_train = "../data/audio/train"
destination_video_folder_val = "../data/video/validation"
destination_audio_folder_val = "../data/audio/validation"
destination_video_folder_test = "../data/video/test"
destination_audio_folder_test = "../data/audio/test"

# for video_id in train_ids:
#     source_video_path = f"{source_video_folder}/{video_id}.mp4"
#     destination_video_path = f"{destination_video_folder_train}/{video_id}.mp4"

#     try:
#         shutil.move(source_video_path, destination_video_path)
#         print(f"Moved {video_id}.mp4 to {destination_video_folder_train}")
#     except FileNotFoundError:
#         print(f"Video {video_id}.mp4 not found in source folder")
#     except Exception as e:
#         print(f"An error occurred while moving {video_id}.mp4: {e}")

# for video_id in val_ids:
#     source_video_path = f"{source_video_folder}/{video_id}.mp4"
#     destination_video_path = f"{destination_video_folder_val}/{video_id}.mp4"

#     try:
#         shutil.move(source_video_path, destination_video_path)
#         print(f"Moved {video_id}.mp4 to {destination_video_folder_val}")
#     except FileNotFoundError:
#         print(f"Video {video_id}.mp4 not found in source folder")
#     except Exception as e:
#         print(f"An error occurred while moving {video_id}.mp4: {e}")

# for video_id in test_ids:
#     source_video_path = f"{source_video_folder}/{video_id}.mp4"
#     destination_video_path = f"{destination_video_folder_test}/{video_id}.mp4"

#     try:
#         shutil.move(source_video_path, destination_video_path)
#         print(f"Moved {video_id}.mp4 to {destination_video_folder_test}")
#     except FileNotFoundError:
#         print(f"Video {video_id}.mp4 not found in source folder")
#     except Exception as e:
#         print(f"An error occurred while moving {video_id}.mp4: {e}")

for audio_id in train_ids:
    source_audio_path = f"{source_audio_folder}/{audio_id}.mp4"
    destination_audio_path = f"{destination_audio_folder_train}/{audio_id}.mp4"

    try:
        shutil.move(source_audio_path, destination_audio_path)
        print(f"Moved {audio_id}.mp4 to {destination_audio_folder_train}")
    except FileNotFoundError:
        print(f"Video {audio_id}.mp4 not found in source folder")
    except Exception as e:
        print(f"An error occurred while moving {audio_id}.mp4: {e}")

for audio_id in val_ids:
    source_audio_path = f"{source_audio_folder}/{audio_id}.mp4"
    destination_audio_path = f"{destination_audio_folder_val}/{audio_id}.mp4"

    try:
        shutil.move(source_audio_path, destination_audio_path)
        print(f"Moved {audio_id}.mp4 to {destination_audio_folder_val}")
    except FileNotFoundError:
        print(f"Video {audio_id}.mp4 not found in source folder")
    except Exception as e:
        print(f"An error occurred while moving {audio_id}.mp4: {e}")

for audio_id in test_ids:
    source_audio_path = f"{source_audio_folder}/{audio_id}.mp4"
    destination_audio_path = f"{destination_audio_folder_test}/{audio_id}.mp4"

    try:
        shutil.move(source_audio_path, destination_audio_path)
        print(f"Moved {audio_id}.mp4 to {destination_audio_folder_test}")
    except FileNotFoundError:
        print(f"Video {audio_id}.mp4 not found in source folder")
    except Exception as e:
        print(f"An error occurred while moving {audio_id}.mp4: {e}")