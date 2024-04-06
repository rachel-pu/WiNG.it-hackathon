import speech_recognition as sr


r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("test it out")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print({text})

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")