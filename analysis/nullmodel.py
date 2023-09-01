import pandas as pd
import numpy as np

train_df = pd.read_csv("../data/dataset/train/train.csv")

null_likes = np.mean(train_df['likes_per_view'])
null_views = np.mean(train_df['views_per_week'])

print("Null Model Likes Per View = " + str(null_likes))
print("Null Model Views Per Week = " + str(null_views))