import pyttsx3

text = 'здравствуйте, увважаемые жюри хакатона! Меня зовут Асима и я голосовой помощник от команды Интеграл. Каждую секунду я могу обучаться отвечать на больше вопросов. Надеюсь, что я вам понравлюсь'
tts = pyttsx3.init()
rate = tts.getProperty('rate') 
tts.setProperty('rate', rate-10)

volume = tts.getProperty('volume') 
tts.setProperty('volume', volume+0.98)

voices = tts.getProperty('voices')


tts.setProperty('voice', 'ru') 


for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

tts.say(text)
tts.runAndWait()
