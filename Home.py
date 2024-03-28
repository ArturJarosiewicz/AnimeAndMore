import streamlit as st

sub = """
Welcome
"""

content = """
A few words about me\n
This app stores and shares my favorite characters from any software. Plus, I like coding, so this is a good excuse
combine business with pleasure. I grew up in the 90's watching almost all animated series and action movies
available on TV/VHS. I played on Nes, Pegasus, PSX, PS2, PS3, Switch, PC and of course GameBoy Pocket.
I hope it will be nice to remind me of all the wonderful stories from the past when I was young during
creating this website. Titles that I have been watching/playing recently will also appear.

This will be similar to a blogging convention. Entries may concern, for example, a single character from a movie or game,
others may focus on an entire series, etc. What I mean is that there won't be a stiff pattern.

Perhaps you will come across an interesting staff that you did not know or have already forgotten.

PS Sorry for syntax or grammtical error (if there will be)
"""

st.subheader(sub)
st.write(content)