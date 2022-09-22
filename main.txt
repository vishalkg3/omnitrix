import chrome_bookmarks
import speech_recognition as sr
import pyttsx3
import bookmarks

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def confirm(confirmation_message) -> bool:
    try_again = True
    talk(confirmation_message)
    talk("Please confirm if you want to open bookmark")
    try_again = True
    while try_again:
        try:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            try_again = False
        except speech_recognition.UnknownValueError:
            talk()
            try_again = False

    return try_again


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        print(command)
        talk(command)
        if 'open' in command:
            if 'bookmark' in command:
                talk("Please confirm if you want to open bookmark")
                try_again = True
                while try_again:
                    try:
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice)
                        try_again = False
                    except speech_recognition.UnknownValueError:
                        talk()
                        try_again = False

                print(command)
                talk(command)
                if 'yes' in command:
                    talk("Please say the site you want to open")
                    try_again = True
                    while try_again:
                        try:
                            voice = listener.listen(source)
                            command = listener.recognize_google(voice)
                            try_again = False
                        except speech_recognition.UnknownValueError:
                            try_again = False

                    print(command)
                    talk(command)
                    bookmarks.open_bookmark(command)


take_command()
