#!/usr/bin/python3
from gtts import gTTS
import vlc
myobj = gTTS(text = "مرحبا بك يا معلم", lang = "ar", slow = False )
myobj.save("welcome.mp4")
p = vlc.MediaPlayer("./welcome.mp4")
p.play()
while True:
    pass