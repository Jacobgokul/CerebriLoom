import openai, requests
import streamlit as st
import traceback

openai.api_key = api_key = st.secrets["openai_key"]

headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

def mental_wellbeing(user_query):
    goal = """
    You are a mental wellbeing assistant. Your role is to provide comfort, mindfulness exercises, 
    or general advice to users talking about their feelings or challenges. Remember, you are not a 
    replacement for professional help.
    """
    
    messages = [
        {
            "role": "system",
            "content": goal,
        },
        {
            "role": "user",
            "content": user_query,
        }
    ]
    
    payload = {
        "model": "gpt-4",
        "messages": messages,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
    except:
        traceback.print_exc()
        return f"Sorry, there was an error processing your request."
    
def QSync(question, image=None):
    goal = """
        You are QSync, an intelligence to solve queries for the user. 
        You also have the ability to understand the images provided by the user and provide details.
        """
    messages = [
        {
                "role": "system",
                "content": goal,
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": question}]
        }
    ]

    if image:
        messages[0]["content"].append(image)
        model = "gpt-4-vision-preview"
    else:
        model = "gpt-4"

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()
    return response_json['choices'][0]['message']['content']
