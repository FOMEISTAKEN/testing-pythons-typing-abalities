import pyttsx3

def speaker():
    speak = input("Type something to turn into speech: ")
    engine = pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()

while True:
    speaker()



