from openai import OpenAI
import streamlit as st
from streamlit_feedback import streamlit_feedback
import trubrics

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="feedback_api_key", type="password")

st.title("📝 Chat with feedback (Trubrics)")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you? Leave feedback to help me improve!"}
    ]
if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Tell me a joke about sharks"):
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    st.session_state["response"] = response.choices[0].message.content
    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": st.session_state["response"]})
        st.write(st.session_state["response"])

if st.session_state["response"]:
    feedback = streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="[Optional] Please provide an explanation",
        key=f"feedback_{len(messages)}",
    )

    if feedback and "TRUBRICS_EMAIL" in st.secrets:
        config = trubrics.init(
            email=st.secrets.TRUBRICS_EMAIL,
            password=st.secrets.TRUBRICS_PASSWORD,
        )
        collection = trubrics.collect(
            component_name="default",
            model="gpt",
            response=feedback,
            metadata={"chat": messages},
        )
        trubrics.save(config, collection)
        st.toast("Feedback recorded!", icon="📝")