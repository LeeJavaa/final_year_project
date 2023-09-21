import pandas as pd
import numpy as np
import re

# train_df = pd.read_csv("../data/dataset/train/train.csv")

# null_likes = np.mean(train_df['likes_per_view'])
# null_views = np.mean(train_df['views_per_week'])

# print("Null Model Likes Per View = " + str(null_likes))
# print("Null Model Views Per Week = " + str(null_views))

null_under_10 = 2.095611365119467
null_over_40 = 1.7516747384990181
null_between = 2.634107794215827

def convert_duration_to_seconds(duration):
    pattern = r'PT(\d+H)?(\d+M)?(\d+S)?'
    hours, minutes, seconds = re.match(pattern, duration).groups()
    
    total_seconds = 0
    if hours:
        total_seconds += int(hours[:-1]) * 3600
    if minutes:
        total_seconds += int(minutes[:-1]) * 60
    if seconds:
        total_seconds += int(seconds[:-1])
    
    return total_seconds

def assign_null_prediction(duration):
    if duration < 600:
        return null_under_10
    elif duration > 2400:
        return null_over_40
    else:
        return null_between

val_df = pd.read_csv("../data/dataset/validation/validation_no_transcript.csv")
val_df['duration_seconds'] = val_df['duration'].apply(convert_duration_to_seconds).values.reshape(-1, 1)
val_df['null_prediction'] = val_df['duration_seconds'].apply(assign_null_prediction).values.reshape(-1, 1)
val_df.to_csv("../data/dataset/models/null/duration.csv", header=True, index=False)