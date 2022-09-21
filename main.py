import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        print(command)


take_command()
