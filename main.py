import streamlit as st
import pandas as pd


df = pd.read_csv('data.csv', sep=';')

st.set_page_config(page_title='Hokuto no Ken')

col1, col2 = st.columns(2)

with col1:
    st.image("images/ken.png")

with col2:
    st.title("Kenshirō")
    content = """
    I'am main protagonist of the Hokuto no Ken manga, anime and related media. 
    I'am a martial artist and the 64th successor of the Hokuto Shinken style and considered one of the greatest 
    successors in its 1,800 year history.
    """
    st.info(content)

st.subheader('If You are a fan you should know below characters')


for index, row in df.iterrows():
    st.subheader(row['name'])
    st.info(row['description'])
    st.image(f"images/{row['image']}")