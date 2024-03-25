import streamlit as st

st.title('Contact me')

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your email")
    user_message = st.text_area("Message")
    button = st.form_submit_button("Submit")

    if button:
        print("Press")