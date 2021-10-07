import speech_recognition as sr
import sys
import webbrowser
import pyttsx3


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk('Привет. Спросите у меня что-то')


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Скажите что- то')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print('Вы сказали: ' + task)
    except sr.UnknownValueError:
        talk("Я вас не понимаю")
        task = command()

    return task


def make_something(task):
    if 'открой youtube' in task:
        talk('Пытаюсь выполнить')
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
    elif 'скажи шутку' in task:
        talk('Подходит сталкер к монолиту. Тот ему говорит: '
             'Ну, давай, загадывай желание. '
             'Хочу чтобы Зона исчезла. '
             'Не, ну это ты загнул так загнул... Давай проси что-нибудь полегче. '
             'Ну, тогда сделай так чтобы Сидорович торговал без обмана. '
             'Так... А что ты там насчёт Зоны говорил?')
    elif 'стоп' in task:
        talk('Да, без проблем')
        sys.exit()


while True:
    make_something(command())
