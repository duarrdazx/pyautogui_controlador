import requests
import pyautogui
import time

# Define o tempo para o usuário focar na janela (bloco de notas, navegador etc)
print("Você tem 5 segundos para posicionar o cursor onde deseja que a frase seja digitada...")
time.sleep(5)

# Faz uma requisição para uma API pública 
url = "https://www.omdbapi.com/?i=tt3896198&apikey=92ef4fe2"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    titulo = dados['Title']
    ano = dados['Year']
    tempo = dados['Runtime']
    genero = dados['Genre']
    diretor = dados['Director']

    # Frase final formatada
    texto = f'"{titulo}"\n— {ano}'

    # Digita usando o pyautogui
    pyautogui.write("Título: " + titulo, interval=0.05)
    pyautogui.press("enter")
    pyautogui.write("Ano: " + ano, interval=0.05)
    pyautogui.press("enter")
    pyautogui.write("Tempo: " + tempo, interval=0.05)
    pyautogui.press("enter")
    pyautogui.write("Gênero: " + genero, interval=0.05)
    pyautogui.press("enter")
    pyautogui.write("Diretor: " + diretor, interval=0.05)

else:
    print("Erro ao obter a frase da API.")
