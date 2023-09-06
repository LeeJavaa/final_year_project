import re
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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

train_df = pd.read_csv("../data/dataset/train/train_no_transcript.csv")
validate_df = pd.read_csv("../data/dataset/validation/validation.csv")

duration_train = train_df['duration'].apply(convert_duration_to_seconds).values.reshape(-1, 1)
X_train = train_df[['comments', 'elapsed_weeks']]
X_train['duration'] = duration_train
# y_train = train_df['likes_per_view']
y_train = train_df['views_per_week']
duration_validation = validate_df['duration'].apply(convert_duration_to_seconds).values.reshape(-1, 1)
X_validate = validate_df[['comments', 'elapsed_weeks']]
X_validate['duration'] = duration_validation

reg = LinearRegression().fit(X_train, y_train)

predictions = reg.predict(X_validate)
print(predictions)

# Model 1
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/1.csv", header=True, index=False)
# linreg_df = pd.read_csv("../data/dataset/models/linreg/1.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/1.csv", header=True, index=False)

# Model 2
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/2.csv", header=True, index=False)
linreg_df = pd.read_csv("../data/dataset/models/linreg/2.csv")
linreg_df['views_per_week_predicted'] = predictions
linreg_df['views_per_week_actual'] = validate_df['views_per_week']
linreg_df.to_csv("../data/dataset/models/linreg/2.csv", header=True, index=False)