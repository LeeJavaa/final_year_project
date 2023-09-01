import pandas as pd

# train_df = pd.read_csv("../data/dataset/train/train.csv")
# clean_df = train_df.drop(['transcript'], axis=1)
# transcript_df = train_df[['id', 'transcript']]
# clean_df.to_csv("../data/dataset/train/train_no_transcript.csv", header=True, index=False)
# transcript_df.to_csv('../data/dataset/train/train_transcript.csv', header=True, index=False)

val_df = pd.read_csv("../data/dataset/validation/validation.csv")
clean_df = val_df.drop(['transcript'], axis=1)
transcript_df = val_df[['id', 'transcript']]
clean_df.to_csv("../data/dataset/validation/validation_no_transcript.csv", header=True, index=False)
transcript_df.to_csv('../data/dataset/validation/validation_transcript.csv', header=True, index=False)