import streamlit as st
from langchain.llms import OpenAI
from openai import RateLimitError
import time

st.title("Chat with OpenAI")

openai_api_key = st.sidebar.text_input("Enter your OpenAI API key")

if openai_api_key.startswith("sk-"):
    llm = OpenAI(api_key=openai_api_key)
else:
    llm = None

def generate_response(input_text):
    try:
        response = llm(input_text)
        st.info(response)
    except RateLimitError:
        st.error("Rate limit exceeded. Please try again later.")
        time.sleep(60)

with st.form(key='my_form'):
    input_text = st.text_area("Enter your message")
    submit_button = st.form_submit_button(label='Submit')

    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter a valid OpenAI API key", icon='⚠')

    if submit_button and openai_api_key.startswith("sk-"):
        generate_response(input_text)