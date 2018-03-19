import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
from pygame import mixer

mixer.init()

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
print("Your Mics Are: \n\n")
print(mic_list)
print("\n")

with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("\nSay Something\n\n")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said: \t" + text)
        speech_analysis = TextBlob(text)
        if speech_analysis.polarity > 0:
            print("\n\nYour Statement was Positive\n\n")
            sentiment = str("Your Statement was Positive")
        elif speech_analysis.polarity < 0:
            print("\n\nYour Statement was Negative\n\n")
            sentiment = str("Your Statement was Negative")
        else:
            print("\n\nYour Statement was Kinda Neutral\n\n")
            sentiment = str("Your Statement was Kinda Neutral")

        tts = gTTS(text="I think you said " +str(text)+" and "+sentiment, lang='en')
        tts.save('response.mp3')
        mixer.music.load('response.mp3')
        mixer.music.play()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio!")
    except sr.RequestError as e:
        print(
            "Could not request resultes from Google Speech Recognition service; {0}".format(e))
wait = input()
