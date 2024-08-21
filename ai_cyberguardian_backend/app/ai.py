import openai

def perform_analysis(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with your model version
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
        ],
    )
    
    result = response['choices'][0]['message']['content']
    return result
