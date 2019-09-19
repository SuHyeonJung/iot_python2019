import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Speak into the microphone")
    audio = r.listen(source, timeout=2)

print("Ready")
try:
    print("Transcription: " + r.recognize_google(audio, language="ko-KO"))
except sr.UnknownValueError:
    print("Audio unintelligible")
except sr.RequestError as e:
    print("Cannot obtain results; {0}".format(e))

