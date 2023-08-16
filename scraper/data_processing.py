import pandas as pd
from datetime import datetime
import numpy as np

df = pd.read_csv('../data/dataset/raw_data.csv')

# Rename dataframe columns
df.rename(columns={
    "snippet.publishedAt": "date",
    "snippet.title" : "title",
    "snippet.description" : "description",
    "contentDetails.duration" : "duration",
    "statistics.viewCount" : "views",
    "statistics.likeCount" : "likes",
    "statistics.commentCount" : "comments"
}, inplace=True)

# Get likes per view
df['likes_per_view'] = (df['likes'] / df['views'])

# Get weeks since upload
current_date = datetime.now()
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%SZ')
df['elapsed_time'] = current_date - df['date']
df['elapsed_weeks'] = (current_date - df['date']) / np.timedelta64(1, 'W') # Note weeks are a floating point value. More accurate.

# Get views per week
df['views_per_week'] = df['views'] / df['elapsed_weeks']

df.to_csv("../data/dataset/data.csv", header=True, index=False)