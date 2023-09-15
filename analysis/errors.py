import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Likes
df = pd.read_csv("../data/dataset/models/linreg/5.csv")

actual_outputs = df['likes_per_view_actual']*100
predicted_outputs = df['likes_per_view_predicted']*100

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(actual_outputs, predicted_outputs)
print("Mean Absolute Error:", mae)

# Calculate Root Mean Squared Error (RMSE)
rmse = mean_squared_error(actual_outputs, predicted_outputs, squared=False)
print("Root Mean Squared Error:", rmse)

# Views
# df = pd.read_csv("../data/dataset/models/linreg/3.csv")

actual_outputs = df['views_per_week_actual']
predicted_outputs = df['views_per_week_predicted']

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(actual_outputs, predicted_outputs)
print("Mean Absolute Error:", mae)

# Calculate Root Mean Squared Error (RMSE)
rmse = mean_squared_error(actual_outputs, predicted_outputs, squared=False)
print("Root Mean Squared Error:", rmse)