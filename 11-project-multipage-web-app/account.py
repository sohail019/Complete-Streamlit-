import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Check if the app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("streamlit-app-70039-5abfe6278624.json")
    firebase_admin.initialize_app(cred)

def app():
    st.title("Account Page")
    
    choice = st.selectbox("Login/Signup", ["Login", "Signup"])

    if "username" not in st.session_state:
        st.session_state.username = ""
    if "email" not in st.session_state:
        st.session_state.email = ""
    if "password" not in st.session_state:
        st.session_state.password = ""

    def f():
        try:
            user = auth.get_user_by_email(email)
            st.success("Login Successful")

            st.session_state.username = user.uid
            st.session_state.email = user.email

        except:
            st.warning("Login failed")

    if "signedout" not in st.session_state:
        st.session_state.signedout = False
    if "signout" not in st.session_state:
        st.session_state.signout = False
        

    if choice == "Login":
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        st.button("Login", on_click=f)
    else:
        username = st.text_input("Username") 
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        if st.button("Create my account"):
            user = auth.create_user(email=email, password=password, uid=username)
            st.success("User created successfully")
            st.markdown("Please login to continue")
            st.balloons()

        