import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def translate_speech():
    # Inicializa o reconhecedor de fala
    r = sr.Recognizer()

    # Define o idioma de entrada como inglês
    with sr.Microphone() as source:
        print("Diga algo em inglês:")
        audio = r.listen(source)

    try:
        # Reconhece a fala em inglês
        text = r.recognize_google(audio)

        # Traduz a frase para o português
        translator = Translator()
        translation = translator.translate(text, dest='pt')
        translated_text = translation.text

        # Inicializa o conversor de texto para fala
        engine = pyttsx3.init()
        engine.say(translated_text)
        engine.runAndWait()

        print("Frase traduzida:", translated_text)

    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
    except sr.RequestError as e:
        print("Erro na solicitação ao serviço de reconhecimento de fala; {0}".format(e))

# Chama a função para traduzir a fala
translate_speech()
