import streamlit as st
import os
from groq import Groq

# Set up the page configuration
st.set_page_config(page_title="Groq Chat App", layout="wide")

# Get API key from secrets.toml
groq_api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=groq_api_key)

# Select Groq model
model = st.sidebar.selectbox("Select a Groq Model", ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it"])

st.title("💬 Groq Chat App")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Construct the messages payload for the API
        messages_payload = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        
        # Stream the response from Groq with the corrected method
        try:
            stream = client.chat.completions.create(
                model=model,
                messages=messages_payload,
                stream=True
            )
            for chunk in stream:
                full_response += chunk.choices[0].delta.content or ""
                message_placeholder.markdown(full_response + "▌")

        except Exception as e:
            st.error(f"An error occurred: {e}")
            full_response = "I'm sorry, an error occurred while processing your request."

        # Finalize the response display
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})