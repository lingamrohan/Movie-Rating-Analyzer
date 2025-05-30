import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'movieId': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Parasite'],
    'genre': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Action', 'Drama'],
    'year': [1999, 2010, 2014, 2008, 2019]
}

ratings = {
    'userId': [101, 102, 103, 104, 105, 106, 107, 108],
    'movieId': [1, 1, 2, 2, 3, 3, 4, 5],
    'rating': [5, 4, 5, 3, 4, 5, 5, 4]
}

# Create DataFrames
movies_df = pd.DataFrame(data)
ratings_df = pd.DataFrame(ratings)

# Merge data
df = pd.merge(ratings_df, movies_df, on='movieId')

# 1. Top-rated movies (average rating)
top_rated = df.groupby('title')['rating'].mean().sort_values(ascending=False)
print("\n🎥 Top Rated Movies:")
print(top_rated)

# 2. Filter by Genre
genre_filter = input("\nEnter a genre to filter (e.g., Sci-Fi, Action, Drama): ")
filtered_by_genre = df[df['genre'].str.lower() == genre_filter.lower()]
print(f"\n🎬 Movies in Genre '{genre_filter}':")
print(filtered_by_genre[['title', 'rating']])

# 3. Average rating by user
avg_rating_user = df.groupby('userId')['rating'].mean()
print("\n👤 Average Rating by User:")
print(avg_rating_user)

# 4. Visualization: Average rating per movie
avg_rating_movie = df.groupby('title')['rating'].mean()
avg_rating_movie.plot(kind='bar', color='skyblue', title='Average Rating per Movie')
plt.xlabel('Movie Title')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.show()
