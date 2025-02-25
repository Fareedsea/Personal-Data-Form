import streamlit as st
import datetime

st.title('User Information Form')

form_values = {
    "Name": None,
    "Address": None,
    "Gender": None,
    "Date_Birth": None,
    "Email": None
}

with st.form(key="user_info_form"):
    form_values["Name"] = st.text_input("Enter Your Name:")
    form_values["Address"] = st.text_input("Enter Your Address:")
    form_values["Gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["Date_Birth"] = st.date_input("Enter Your Birthday", min_value=datetime.date(1900, 1, 1), max_value='today')
    form_values["Email"] = st.text_input("Enter Your Email Address")

    submit_button = st.form_submit_button(label="Submit")     

if submit_button:
    # Note: The check below might flag a value of 0.0 as missing.
    if not all(form_values.values()):
        st.warning("Please fill in all of the fields")
    else:
        st.balloons()
        st.write("## Personal Information")
        
        for key, value in form_values.items():
            st.write(f"{key}: {value}")