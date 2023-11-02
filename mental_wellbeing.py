import openai


openai.api_key = "" #Replace openAI key


import openai

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
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Sorry, there was an error processing your request. Error: {e}"