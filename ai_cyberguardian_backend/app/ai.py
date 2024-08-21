# app/ai.py
import openai
from flask import current_app

def perform_analysis(text):
    with current_app.app_context():
        openai.api_key = current_app.config['OPENAI_API_KEY']
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity expert."},
                {"role": "user", "content": text}
            ]
        )
        return response['choices'][0]['message']['content']
