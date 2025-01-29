import streamlit as st
from langchain.llms import OpenAI
from openai import RateLimitError
import time

st.title("Chat with OpenAI")

# openai_api_key = st.sidebar.text_input("Enter your OpenAI API key")

openai_api_key = "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"

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