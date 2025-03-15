import requests

url = 'https://jsonplaceholder.typicode.com/comments'
params = {"postId" :1 }# obter apenas comentarios do postid=1
resposta = requests.get(url, params=params)

comentarios = resposta.json()
print(f'Foram encontrados {len(comentarios)} comentarios.')
print(f'Erro: {resposta.status_code} - {resposta.text}')