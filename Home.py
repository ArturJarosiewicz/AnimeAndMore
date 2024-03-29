import streamlit as st

sub = """
Welcome
"""

content = """
A few words about me and app\n
This app stores and shares my favorite characters from any universe. Plus, I like coding, so this is a good excuse to
combine business with pleasure. I grew up in the 90's watching almost all animated series and action movies
available on TV/VHS. I played on Nes, Pegasus, PSX, PS2, PS3, Switch, PC and of course GameBoy Pocket.
I hope it will be nice to remind me of all the wonderful stories from the past when I was young during
creating this website. Titles that I have been watching/playing recently will also appear.

This will be similar to a blogging convention. Entries may contain, for example, a single character from a movie or game,
others may focus on an entire series, etc. What I mean is that there won't be a stiff pattern.

Perhaps you will come across an interesting staff that you did not know or have already forgotten.

PS Sorry for syntax or grammtical error (if there will be)
"""
st.set_page_config(
    page_title="Anime and more",
    layout="wide",
    menu_items={
       'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
        }
)

st.image(image='images/home_banner.png')
st.subheader(sub)
st.write(content)

st.title('Contact me')

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your email")
    user_message = st.text_area("Message")
    button = st.form_submit_button("Send")

    if button:
        print("Press")