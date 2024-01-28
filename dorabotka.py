from openai import OpenAI
import json
client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)
import pyttsx3
import speech_recognition as sr

tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', rate-20)
volume = tts.getProperty('volume')
tts.setProperty('volume', volume+0.9)
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=1) 
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {query.lower()}')
        textMessage( text )
    except:
        print('Ошибка распознавания.')

def talk( text ):
    tts.say( text )
    tts.runAndWait()

def textMessage( text ):
    request = openai.ApiAI('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').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = '20' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем пользователю, если нет - бот его не понял
    if response:
        request.audio_output = response
        talk(response)
    else:
        talk('Простите. Я Вас не совсем поняла.')

while True:
    record_volume()