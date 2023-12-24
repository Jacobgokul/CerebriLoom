import base64
import streamlit as st
from utilities.ai_utils import mental_wellbeing, QSync

# Sidebar
st.sidebar.title("AI Assitant")
assistant = st.sidebar.selectbox("Select the Assistant", options=["MindEase", "QSync"])
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

elif assistant == 'QSync':
    st.title(":red[Q]:blue[Sync]")
    st.info("I'm here to help you out with your queries")

    # Initialize chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Share your thoughts, I'm here to listen.")
    uploaded_file = st.file_uploader("Upload a file", type=["jpg", "png", "jpeg"])

    def encode_image(uploaded_file):
        file_bytes = uploaded_file.getvalue()
        return base64.b64encode(file_bytes).decode('utf-8')

    if user_input:
        image = None
        if uploaded_file is not None:
            base64_image = encode_image(uploaded_file)
            image = {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }

        # Placeholder for AI response function
        ai_response = QSync(user_input, image)  # Replace with actual function call

        # Add user message and AI response as a pair to chat history
        st.session_state.chat_history.append({"user": user_input, "ai": ai_response})

    # Display chat history
    for message_pair in st.session_state.chat_history:
        st.write(f"You: {message_pair['user']}")
        st.write(f"AI: {message_pair['ai']}")

else:
    st.header(":red[Cerebri]:blue[Loom]")
