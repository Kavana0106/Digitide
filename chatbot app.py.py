import streamlit as st
import time

# ---- Page Config ----
st.set_page_config(page_title="Simple Chat App", page_icon="🤖", layout="centered")
st.title("🤖 Simple Chat App (No API Key)")

# ---- Session State for Messages ----
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ---- Rule-based chatbot dictionary ----
responses = {
    "hi": "Hello! 👋",
    "hello": "Hi there! 😊",
    "hey": "Hey! How’s it going?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "bye": "Goodbye! Have a wonderful day! 👋",
}

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    return responses.get(user_input, f"I don’t understand '{user_input}', but I’m learning! 🤖")

# ---- Display Previous Messages ----
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- User Input ----
if prompt := st.chat_input("Type your message..."):
    # Store and display user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        response_text = chatbot_response(prompt)

        # Simulate typing effect (streaming)
        for word in response_text.split():
            full_response += word + " "
            time.sleep(0.1)
            response_container.markdown(full_response)

        # Store assistant message
        st.session_state["messages"].append({"role": "assistant", "content": full_response})
