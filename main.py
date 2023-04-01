import time
import pyperclip
import pyautogui

# Attendi 10 secondi prima di iniziare lo script (non modificare)
time.sleep(10)

# Apri il file "spam" e leggi le linee del file
with open("spam", "r") as f:
    lines = f.readlines()

# Ciclo infinito
while True:
    # Itera attraverso le linee del file
    for line in lines:
        # Copia la linea nella clipboard
        pyperclip.copy(line.strip())

        # Simula la pressione dei tasti "cmd+c i a o" per incollare il contenuto della clipboard
        pyautogui.hotkey('command', "c", "i", "a", "o", interval=0)
        #Metti la parola che vuoi lettera per lettera ( es: "c", "a", "p", "r", "a" )


        # Invia un tasto invio per inviare il messaggio
        pyautogui.typewrite("\n")

    # Attendi 1 secondo prima di ripetere il ciclo
    time.sleep(1)