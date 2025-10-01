# import pandas as pd
# import pickle

# # Load CSVs
# movies = pd.read_csv('tmdb_5000_movies.csv')
# credits = pd.read_csv('tmdb_5000_credits.csv')

# # Merge datasets
# movies = movies.merge(credits, on='title')

# # Select and preprocess columns
# movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# # Save as pickle
# pickle.dump(movies, open('movie_data.pkl','wb'))

import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Load CSVs
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge datasets
movies = movies.merge(credits, on='title')

# Select required columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# Helper function to convert stringified lists into python objects
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies.dropna(inplace=True)

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

movies['crew'] = movies['crew'].apply(fetch_director)
movies['cast'] = movies['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)][:3])

movies['overview'] = movies['overview'].apply(lambda x:x.split())

# Combine all tags
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
new_df = movies[['movie_id','title','tags']]

# Convert list to string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df['tags'] = new_df['tags'].str.lower()

# Vectorize
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Cosine similarity
cosine_sim = cosine_similarity(vectors)

# ✅ Save both movies and cosine_sim
pickle.dump((new_df, cosine_sim), open('movie_data.pkl','wb'))
