import streamlit as st
from mental_wellbeing import mental_wellbeing

# Sidebar
st.sidebar.title("AI Assitant")
assistant = st.sidebar.selectbox("Select the Assistant", options=["MindEase", "Blank"])
clear_chat = st.sidebar.button("Clear Chat")

if clear_chat:
    st.session_state.chat_history = []

# Initialize session state for chat if not present
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


if assistant == 'MindEase':
    st.title(":red[Mind]:blue[Ease]")
    st.info("Lean on me, and let's find calmness together.")
    # User input
    user_input = st.chat_input(placeholder="Share your thoughts, I'm here to listen.")
    # Check if user entered a message
    if user_input:
        # Get AI response
        ai_response = mental_wellbeing(user_input)
        
        # Add user message and AI response as a pair to chat history
        st.session_state.chat_history.append({"user": user_input, "ai": ai_response})

    # Display chat history
    for message_pair in st.session_state.chat_history:
        st.write(f"You: {message_pair['user']}")
        st.write(f"AI: {message_pair['ai']}")
else:
    st.header(":red[Cerebri]:blue[Loom]")
