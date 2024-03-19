import tkinter as tk
import requests



# URL para o endpoint de login
url_login = 'http://192.168.10.197/login.fcgi'

# Dados de login
dados_login = {
    "login": "teste",
    "password": "admin"
}

response = requests.post(url_login, json=dados_login)


if response.status_code == 200:
    print("Sessão iniciada com sucesso!")
    
    # Verificando se o código da sessão está presente na resposta
    if 'session_code' in response.json():
        session_code = response.json()['session_code']
        print("Código da sessão:", session_code)
    else:
        print("Código da sessão não encontrado na resposta.")
else:
    print("Erro ao iniciar a sessão:", response.text)