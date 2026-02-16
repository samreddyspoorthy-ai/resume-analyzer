import openai

openai.api_key = "YOUR_API_KEY"

def get_ai_feedback(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user",
             "content":f"Give suggestions to improve this resume:\n{text}"}
        ]
    )

    return response.choices[0].message.content
