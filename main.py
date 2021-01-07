# Codes for converting the Text to Speech and Saving the file as well
# pip install gTTs >>> if not available
# to speech conversion
from gtts import gTTS

# This module is imported so that we can play the converted audio
import os

# Type the text which you wanted to convert in voice speech
mytext = 'Welcome Home. How are you. '

# Language in which you want to convert
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=True) #slow=False)

# Saving the file
myobj.save("welcome.mp3")

# Play the converted file
os.system("start welcome.mp3")

#***********************************************************
# Below is the codes for Converting and Playing the Text to Speech without Saving the MP3 files.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello. How are you doing today? Welcome to Demo Session")
engine.runAndWait()
