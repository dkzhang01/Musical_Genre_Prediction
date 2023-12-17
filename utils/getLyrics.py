import pandas as pd
import os
from lyricsgenius import Genius
import concurrent.futures

token = "90aPABwZpeWFT6QP6an4i7dzqj59_Lcb8ztNBjwDLiuLI43raibRZY-QHm4Xqa7q"
genius = Genius(token)

data = pd.read_csv("./music_genre.csv")
data['lyrics'] = ''

def write_row(row):
    if len(data.at[row, 'lyrics']) == 0:
        track = data.iloc[row]["track_name"]
        artist = data.iloc[row]["artist_name"]
                                
        song = genius.search_song(track, artist)
        if song is not None:
            data.at[row, 'lyrics'] = str(song.lyrics)
        
num_threads = 10

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(write_row, index) for index, row in data.iterrows()]
        
data[["artist_name", "track_name", "music_genre", "lyrics"]].to_csv('music_genre_lyrics.csv', index=False)