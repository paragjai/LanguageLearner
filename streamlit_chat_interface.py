import streamlit as st

st.write("How do I say the following in French?")
user_input = st.text_input("How do I say the following in French?")
print("User input :", user_input)
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right
