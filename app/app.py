import streamlit as st
import pickle
import os

# Load saved model files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = pickle.load(
    open(os.path.join(BASE_DIR, "../models/movie_list.pkl"), "rb")
)

top_similar = pickle.load(
    open(os.path.join(BASE_DIR, "../models/top_similar.pkl"), "rb")
)

# Recommendation function
def recommend(movie):

    matched_indices = movies.index[movies["title"] == movie]

    if len(matched_indices) == 0:
        return []

    movie_index = movies.index.get_loc(matched_indices[0])

    similar_movies = top_similar[movie_index][:5]

    recommendations = []

    for movie_idx, score in similar_movies:
        recommendations.append(movies.iloc[movie_idx].title)

    return recommendations


# Streamlit interface
st.title("🎬 Movie Recommendation System")

st.write("Discover movies similar to your favourites!")

selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")

    for movie in recommendations:
        st.write("🍿", movie)