import openai, requests
import traceback

class AIUtils:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def mental_wellbeing(self, user_query):
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
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=payload)
            return response.json()['choices'][0]['message']['content']
        except:
            traceback.print_exc()
            return f"Sorry, there was an error processing your request."

    def QSync(self, question, image=None):
        try:
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
                messages[1]["content"].append(image)
                model = "gpt-4-vision-preview"
            else:
                model = "gpt-4"

            payload = {
                "model": model,
                "messages": messages,
                "max_tokens": 300
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=payload)
            response_json = response.json()
            return response_json['choices'][0]['message']['content']
        except:
            traceback.print_exc()
            return "Qsync: Oops! There is an error while processing your request"
