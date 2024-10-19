import pandas as pd
import streamlit as st
import pickle
import requests

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similar[movie_index]
    movies_sort = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in movies_sort:
        movie_id = movies.iloc[i[0]].title
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similar = pickle.load(open("C:\Users\Peddi Tarun Tej\Desktop\rms.streamlit\rms.streamlit\similarity.pkl", 'rb'))
movies = pd.DataFrame(movie_dict)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    "The Movie You Watched",
    movies['title'].values
)
if st.button("Recommend"):
    names= recommend(selected_movie_name)
    for i in names:
        st.header(i)
