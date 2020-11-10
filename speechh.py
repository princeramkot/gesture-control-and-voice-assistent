import speech_recognition as sr     # import the library
import subprocess as sp
import webbrowser
import os
#import vlc
import glob
import ctypes


url="www.google.com"
firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
vlc_path="C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
song_path="C:\\Users\prince\Desktop\Fav.mp3"
song_locations="C:\\Users\\prince\\Music\\"



os.chdir(r"C:\\Users\\prince\\Music\\")
mylist = [f for f in glob.glob("*.mp3")]

newlist=[]
for k in mylist:
   newlist.append(k[:-4])


r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    ctypes.windll.user32.MessageBoxW(0, "Speak Anything", "Speech", 1)
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio).casefold()
        if ("notepad" in text):
            if("open" in text or "start" in text):
                programName = "notepad.exe"
                fileName = "file.txt"
                sp.Popen([programName, fileName])
            elif ("close" in text or "stop" in text or "exit" in text):
                os.system("TASKKILL /F /IM notepad.exe")
        elif("firefox" in text):
            if ("open" in text or "start" in text):
                webbrowser.get(firefox_path).open(url)
            elif ("close" in text or "stop" in text or "exit" in text):
                os.system("TASKKILL /F /IM chrome.exe")
        elif ("vlc" in text or "play" in text):
            if ("open" in text or "start" in text or "play" in text):
                for s in newlist:
                    
                    if (s in text):
                        print("match")
                        P = sp.Popen([vlc_path, song_locations + s + ".mp3"])
                        break
            elif ("close" in text or "stop" in text or "exit" in text):
                os.system("TASKKILL /F /IM vlc.exe")
            else:
                P=sp.Popen([vlc_path,song_path])

        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
