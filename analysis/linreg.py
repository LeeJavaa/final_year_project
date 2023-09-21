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
train_audio_df = pd.read_csv("../data/dataset/train/train_audio_clean.csv")
validate_audio_df = pd.read_csv("../data/dataset/validation/validation_audio_clean.csv")
train_audio2_df = pd.read_csv("../data/dataset/train/train_audio2.csv")
validate_audio2_df = pd.read_csv("../data/dataset/validation/validation_audio2.csv")
train_visual_df = pd.read_csv("../data/dataset/train/train_visual.csv")
validate_visual_df = pd.read_csv("../data/dataset/validation/validation_visual.csv")

# Merging in audio and visual data
train_df = train_df.merge(train_visual_df, on='id')
train_df = train_df.merge(train_audio_df, on='id')
train_df = train_df.merge(train_audio2_df, on='id')
validate_df = validate_df.merge(validate_visual_df, on='id')
validate_df = validate_df.merge(validate_audio_df, on='id')
validate_df = validate_df.merge(validate_audio2_df, on='id')
# print(train_df)
# print(validate_df)

# Some processing and setting training and prediction cols
# duration_train = train_df['duration'].apply(convert_duration_to_seconds).values.reshape(-1, 1)
X_train = train_df[['speech_rate', 'pitch_mean', 'colorfulness']]
# X_train['duration'] = duration_train
# y_train = train_df['likes_per_view']
y_train = train_df['views_per_week']
# duration_validation = validate_df['duration'].apply(convert_duration_to_seconds).values.reshape(-1, 1)
X_validate = validate_df[['speech_rate', 'pitch_mean', 'colorfulness']]
# X_validate['duration'] = duration_validation


# Fitting and predicting the linear regression model
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
# linreg_df = pd.read_csv("../data/dataset/models/linreg/2.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/2.csv", header=True, index=False)

# Model 3
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/3.csv", header=True, index=False)
# linreg_df = pd.read_csv("../data/dataset/models/linreg/3.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/3.csv", header=True, index=False)

# Model 3.2
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/3_2.csv", header=True, index=False)
# linreg_df = pd.read_csv("../data/dataset/models/linreg/3_2.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/3_2.csv", header=True, index=False)

# Model 4
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/4.csv", header=True, index=False)
# linreg_df = pd.read_csv("../data/dataset/models/linreg/4.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/4.csv", header=True, index=False)

# Model 5
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/5.csv", header=True, index=False)
# linreg_df = pd.read_csv("../data/dataset/models/linreg/5.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/5.csv", header=True, index=False)

# Model 5.2
# linreg_df = pd.DataFrame(columns=['id', 'likes_per_view_predicted', 'likes_per_view_actual'])
# linreg_df['id'] = validate_df['id']
# linreg_df['likes_per_view_predicted'] = predictions
# linreg_df['likes_per_view_actual'] = validate_df['likes_per_view']
# linreg_df.to_csv("../data/dataset/models/linreg/6.csv", header=True, index=False)
# linreg_df = pd.read_csv("../data/dataset/models/linreg/6.csv")
# linreg_df['views_per_week_predicted'] = predictions
# linreg_df['views_per_week_actual'] = validate_df['views_per_week']
# linreg_df.to_csv("../data/dataset/models/linreg/6.csv", header=True, index=False)