import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list_5 = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movie_list_5:
        movies_id = i[0]
        #fetch poster

        recommended_movies.append((movies.iloc[i[0]].title))
    return recommended_movies,

movies = pickle.load(open('movies.pkl', 'rb'))

movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Enter the movie you would like to watch",
                      movies_list)

if st.button('recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

