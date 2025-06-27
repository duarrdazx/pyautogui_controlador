import pyautogui
import time

# Pausa entre ações
pyautogui.PAUSE = 0.7
pyautogui.FAILSAFE = True

# Parâmetros configuráveis
x_processo = 1925               # X fixo para clicar no processo
y_inicial_processo = 329        # Y do primeiro processo
quantidade_processos = 50       # Total de processos

# Abrir navegador
pyautogui.click(x=2460, y=1053)
time.sleep(1)

for i in range(quantidade_processos):

    # Clicar no processo atual
    pyautogui.click(x=2210, y=329)
    time.sleep(0.1)

    # Abrir fluxo
    pyautogui.click(x=3048, y=434)
    time.sleep(0.7)

    # Cancelar processo
    pyautogui.click(x=3164, y=190)
    time.sleep(0.7)

    # Escrever motivo de cancelamento
    pyautogui.press("tab")
    time.sleep(0.2)
    pyautogui.press("tab")
    time.sleep(0.2)
    pyautogui.write("Cancelamento por motivo de problema no robo!")
    time.sleep(1)

    # Confirmar cancelamento
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.5)

    # Voltar à tela anterior
    pyautogui.click(x=1707, y=186)
    time.sleep(0.5)

    # Clicar para atualizar a lista de processos
    pyautogui.click(x=3159, y=187) 
    time.sleep(0.2)