import streamlit as st
import time

# ---- Page Config ----
st.set_page_config(page_title="Simple Chat App", page_icon="🤖", layout="centered")
st.title("🤖 Simple Chat App (No API Key)")

# ---- Session State for Messages ----
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ---- Simple rule-based chatbot ----
def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How are you?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! 😊"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day! 👋"
    else:
        return f"You said: {user_input}"

# ---- Display Previous Messages ----
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- User Input ----
if prompt := st.chat_input("Type your message..."):
    # Store user message
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        response_text = chatbot_response(prompt)

        # Simulate typing effect
        for word in response_text.split():
            full_response += word + " "
            time.sleep(0.1)
            response_container.markdown(full_response)

        # Store assistant message
        st.session_state["messages"].append({"role": "assistant", "content": full_response})
