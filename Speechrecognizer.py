import speech_recognition as sr

r = sr.Recognizer

with sr.Microphone()  as source:
    text = r.listen(source)

    try:
        rcognised_text = r.recognize_google(text)
        print('recognised_text')
    except sr.UnknownValueError:
            print("")
    except sr.RequestError as e:
            print("")
