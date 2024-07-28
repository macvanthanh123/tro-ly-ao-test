import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    print("Please speak now...")
    # Read the audio data from the default microphone
    audio_data = r.listen(source, timeout=5, phrase_time_limit=5)
    print("Recognizing...")

    try:
        # Convert speech to text
        text = r.recognize_google(audio_data, language="vi")
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
