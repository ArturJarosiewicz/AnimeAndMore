import streamlit as st

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