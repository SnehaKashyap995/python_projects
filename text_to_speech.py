#import the required module for text to speech conversion
from gtts import gTTS

#import the module to play the converted audio
import os

#the text that we want to convert to audio
mytext=input("Enter a string:")

language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("Welcome.mp3")
os.system("start Welcome.mp3")