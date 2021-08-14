import pyttsx3

speaker=pyttsx3.init()
#word per minute(wpm)
speaker.setProperty('rate', 120)

sound=speaker.getProperty('voices')
speaker.setProperty('voice', sound[1].id)

while True:
    answer=input('Enter what you want the speaker to say: \n')
    speaker.say(answer)
    speaker.runAndWait()
