import openai
# API anahtarınızı buraya ekleyin
api_key = open("api_key.txt", "r").read()

# OpenAI API'sine bağlan
openai.api_key = api_key

# Sohbet başlatma
def chat(prompt, model="gpt-3.5-turbo-1106", max_tokens=50):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response.choices[0].message["content"]

# Kullanıcıdan giriş al
user_input = input("Başlamak için bir şeyler yazın: ")

# ChatGPT ile sohbet etme
while user_input.lower() != 'quit':
    response = chat(user_input)
    print(response)
    user_input = input()