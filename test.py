import streamlit as st

st.title(":blue[Python MCQ TEST]")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False
st.header("Do you want to Test your Python Knowledge? (yes/no): ")
def Yes_click_button():
    st.session_state.clicked = True
st.button('Yes', on_click=Yes_click_button)
def No_click_button():
    st.session_state.clicked = False
st.button('No', on_click=No_click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.subheader("Okay! Let's Test:)")
else: 
    quit()    
 