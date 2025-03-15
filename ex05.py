import requests
import json # para enviar dados
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

url = 'https://api.openai.com/v1/chat/completions'

headers= {
    "Content-Type" : "application/json",
    "Authorization":f"Bearer {openai_api_key}"
}

response = requests.get(url, headers=headers)
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json()['choices'][0]['message']['content'])



