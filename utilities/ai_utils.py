import openai, requests
import streamlit as st

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
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Sorry, there was an error processing your request. Error: {e}"
    
def QSync(question, image=None):
    messages = [{
        "role": "user",
        "content": [{"type": "text", "text": question}]
    }]

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
