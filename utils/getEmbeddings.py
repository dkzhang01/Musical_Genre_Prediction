import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
import numpy

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

data = pd.read_csv('./music_genre_lyrics.csv')

def get_bert_embeddings(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)

    outputs = model(**inputs)

    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()

    return embeddings

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name).to(device)

embeddings_list = []
for i in range(len(data)):
    song_lyrics = data.iloc[i]['lyrics']

    if ((not pd.isna(song_lyrics)) and (len(song_lyrics) > 1000)):
        embeddings = get_bert_embeddings(song_lyrics[(len(song_lyrics) // 2):], model, tokenizer)
        embeddings_list.append(embeddings.detach().cpu().numpy())
    else:
        embeddings_list.append(pd.NA)
    print("[%d/%d] rows" % (i, len(data)))
    
data['embeddings'] = embeddings_list
data.to_csv('music_genre_lyrics_embedding.csv', index=False)