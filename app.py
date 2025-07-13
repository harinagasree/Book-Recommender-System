import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

st.set_page_config(layout = "wide")

st.header("Book Recommender System")

st.markdown(""" 
               ##### This system suggests books based on collaborative filtering method
               ##### It presents you with the most suitable books.""")

books = pkl.load(open('books.pkl', 'rb'))
popular = pkl.load(open('popular.pkl', 'rb'))
pt = pkl.load(open('pt.pkl', 'rb'))
similarity_scores = pkl.load(open('similarity_scores.pkl', 'rb'))   # similarity_scores.pkl

st.sidebar.title("Top 50 Books")
# presents the 50 top most popular books
if st.sidebar.button("SHOW"):
    cols = 5
    rows = 10
    for row in range(rows):
        column = st.columns(cols)
        for col in range(cols):
            book_idx = row * cols + col
            if book_idx < len(popular):
                with column[col]:
                    st.image(popular.iloc[book_idx]['Image-URL-M'])
                    st.text(popular.iloc[book_idx]['Book-Title'])
                    st.text(popular.iloc[book_idx]['Book-Author'])


# Recommend books

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key = lambda  x: x[1], reverse=True)[1:6]
    # populate the book information
    data = []
    for i in similar_items:
        item = []
        score_df_name = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(score_df_name.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(score_df_name.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(score_df_name.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return data

# choice for the users - book name to select
book_list = pt.index.values

st.sidebar.title("Similar Book suggestions")

selected_book = st.sidebar.selectbox("Please select a book from the dropdown: ", book_list)

if st.sidebar.button("RECOMMEND ME"):
    book_recommend = recommend(selected_book)
    column = st.columns(5)
    for col_idx in range(5):
        with column[col_idx]:
            if col_idx < len(book_recommend):
                st.image(book_recommend[col_idx][2])
                st.text(book_recommend[col_idx][0])
                st.text(book_recommend[col_idx][1])
