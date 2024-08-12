import streamlit as st
import pandas as pd

@st.cache
def load_data():
    # Replace 'movies.csv' with the path to your dataset
    df = pd.read_csv('movies.csv')
    return df

df = load_data()

st.title("Media & Entertainment Suggestion App")

query = st.text_input("Enter keywords (e.g., Action, Sci-Fi):")

if query:
  
    keywords = query.lower().split(", ")
    df['match'] = df['description'].apply(lambda x: any(keyword in x.lower() for keyword in keywords))


    suggestions = df[df['match']]

    if not suggestions.empty:
        st.subheader("We found some suggestions for you:")
        for index, row in suggestions.iterrows():
            st.write(f"**Title:** {row['title']}")
            st.write(f"**Description:** {row['description']}")
            st.write(f"**Genres:** {row['genres']}")
            st.write("---")
    else:
        st.write("No suggestions found. Try different keywords.")
