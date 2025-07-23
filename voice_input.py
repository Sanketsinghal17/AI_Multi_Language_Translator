import speech_recognition as sr

def record_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        return "❌ Could not understand audio."
    except sr.RequestError as e:
        return f"❌ Speech recognition failed: {e}"
