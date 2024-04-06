import speech_recognition as sr

r = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print("say something")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        text = text.lower()

        print(f"recognized text: {text}")
