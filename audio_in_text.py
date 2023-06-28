import speech_recognition as sr
from reportlab.pdfgen import canvas
import textwrap

def Reconhecer_Fala():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa")
        audio = microfone.listen(source)
        try:
            text = microfone.recognize_google(audio, language="pt-BR")
            print(f"""
            texto: {text}. """, end='\n')
        except:
            print("Não entendi o que você quis dizer.")
            text = ""

        return text

def criar_pdf(texto):
    c = canvas.Canvas("exemplo.pdf")
    lines = textwrap.wrap(texto, width=50)  # Define o limite de caracteres por linha
    y = 750  # Posição vertical inicial
    for line in lines:
        c.drawString(100, y, line)
        y -= 20  # Espaçamento entre as linhas
    c.save()

# Chamada da função de reconhecimento de fala
texto_falado = Reconhecer_Fala()

# Criação do PDF com o texto reconhecido
criar_pdf(texto_falado)
