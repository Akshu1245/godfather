import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def handle_instruction(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the Godfather agent who helps automate any task given by the user."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']
 
