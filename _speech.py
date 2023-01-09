import speech_recognition as sr
from gtts import gTTS
#import os
voice = ""''
while True:
    e = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = e.listen(source)
            text = e.recognize_google(audio)
            print(text)
            if text == 'ok bye':
                break
            text = e.recognize_google(audio)
            voice = voice+str(text)
        except:
            print('voice not audible')
        
we = gTTS(text=voice,lang='en',slow=False)
we.save('./audios/myVoice.wav')       


