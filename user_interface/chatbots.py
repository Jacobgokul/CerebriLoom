import base64
import streamlit as st
from utilities.ai_utils import AIUtils

def display_chatbot_interface(assistant):
    if assistant == 'MindEase':
        st.title(":red[Mind]:blue[Ease]")
        st.info("Lean on me, and let's find calmness together.")
        user_input = st.chat_input(placeholder="Share your thoughts, I'm here to listen.")
        if user_input:
            ai_call = AIUtils(st.session_state.secret_key)
            ai_response = ai_call.mental_wellbeing(user_input)
            st.session_state.chat_history.get(assistant, []).append({"user": user_input, "ai": ai_response})

        # Display chat history
        for message_pair in st.session_state.chat_history[assistant]:
            st.write(f"You: {message_pair['user']}")
            st.write(f"AI: {message_pair['ai']}")

    elif assistant == 'QSync':
        st.title(":red[Q]:blue[Sync]")
        st.info("I'm here to help you out with your queries")

        user_input = st.chat_input(placeholder="Share your thoughts, I'm here to listen.")
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

            ai_call = AIUtils(st.session_state.secret_key)
            ai_response = ai_call.QSync(user_input, image) 
            st.session_state.chat_history.get(assistant, []).append({"user": user_input, "ai": ai_response})

        for message_pair in st.session_state.chat_history[assistant]:
            st.write(f"You: {message_pair['user']}")
            st.write(f"AI: {message_pair['ai']}")

    else:
        st.header(":red[Cerebri]:blue[Loom]")
