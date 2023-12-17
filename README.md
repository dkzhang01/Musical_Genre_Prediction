The dataset, taken from [Kaggle](https://www.kaggle.com/datasets/vicsuperman/prediction-of-music-genre), consisted of 50,000 observations, each representing an audio track that had been uploaded to Spotify. These observations were divided evenly into ten groups of 5,000 for each response class, recorded in the music_genre variable.

STOR 565 Project.pdf contains the original analysis on this dataset.

lyric_analysis.ipynb is an extended report which explores if the lyrics of the song can be used as a more accurate predictor.

The folder utils contains python scripts to generate an extended csv file that contains lyrics and bert-base-uncased embeddings for these lyrics.
