import streamlit as st
from user_interface.chatbots import display_chatbot_interface

# Sidebar
st.sidebar.title("AI Assistant")
assistant = st.sidebar.selectbox("Select the Assistant", options=["CerebriLoom", "MindEase", "QSync"])
clear_chat = st.sidebar.button("Clear Chat")

if clear_chat:
    st.session_state.chat_history[assistant] = []

# Initialize session state for chat if not present
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {"MindEase": [], "QSync": [], "CerebriLoom": []}

# Secret key input
if 'secret_key' not in st.session_state:
    st.session_state.secret_key = ""

def set_secret_key():
    st.session_state.secret_key = st.session_state.temp_secret_key

st.sidebar.text_input("Enter Secret Key", type="password", key="temp_secret_key", on_change=set_secret_key)

# Display appropriate chatbot interface
display_chatbot_interface(assistant)
