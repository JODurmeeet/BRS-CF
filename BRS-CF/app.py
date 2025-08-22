import streamlit as st
import pickle
import numpy as np
import os

# -------------------------
# File Paths with BASE_DIR
# -------------------------
BASE_DIR = r"C:\Users\urmee\Desktop\Python\BRS-CF"

popular_df = pickle.load(open(os.path.join(BASE_DIR, "popular.pkl"), "rb"))
pt = pickle.load(open(os.path.join(BASE_DIR, "pt.pkl"), "rb"))
books = pickle.load(open(os.path.join(BASE_DIR, "books.pkl"), "rb"))
similarity_scores = pickle.load(open(os.path.join(BASE_DIR, "similarity_scores.pkl"), "rb"))

# -------------------------
# Streamlit App
# -------------------------
st.set_page_config(page_title="📚 Book Recommender", layout="wide")
st.title("📚 Book Recommendation System")

tab1, tab2 = st.tabs(["🔥 Popular Books", "🎯 Recommendations"])

# -------------------------
# Tab 1: Popular Books
# -------------------------
with tab1:
    st.subheader("Top 50 Most Popular Books")
    cols = st.columns(5)   # 5 books per row

    for i, row in enumerate(popular_df.iterrows()):
        book = row[1]
        with cols[i % 5]:
            st.image(book["Image-URL-M"], use_column_width=True)
            st.write(f"**{book['Book-Title']}**")
            st.caption(f"✍️ {book['Book-Author']}")
            st.caption(f"⭐ {round(book['avg_rating'], 2)} | {book['num_ratings']} votes")

# -------------------------
# Tab 2: Recommendations
# -------------------------
with tab2:
    st.subheader("Find Similar Books")
    user_input = st.text_input("🔍 Enter a book name you like:")

    if st.button("Recommend"):
        if user_input in pt.index:
            index = np.where(pt.index == user_input)[0][0]
            similar_items = sorted(list(enumerate(similarity_scores[index])),
                                   key=lambda x: x[1], reverse=True)[1:6]

            cols = st.columns(5)
            for i, item in enumerate(similar_items):
                temp_df = books[books['Book-Title'] == pt.index[item[0]]]
                book_title = temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0]
                book_author = temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0]
                book_image = temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0]

                with cols[i % 5]:
                    st.image(book_image, use_column_width=True)
                    st.write(f"**{book_title}**")
                    st.caption(f"✍️ {book_author}")
        else:
            st.error("⚠️ Book not found in dataset. Please try another one!")
