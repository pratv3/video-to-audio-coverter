from moviepy.editor import *
import os
import time
os.system("cls")
print("devloped by pratv3 or prateek vyas with moviepy collabration")
print("https://www.github.com/pratv3")
print("you have to know programming and this is an open source project")
print("this is a video to audio converter build on python")
time.sleep(5)
print(os.system("cls"))
os.system("color f0")
print("________________________video with extension_____________________________")
video=input("enter text here or name of the video")
print("________________________Audio filename wihout extension__________________")
audio=input("enter your text here name of the audio without the extension")
vid=VideoFileClip(video)
aud=vid.audio
aud.write_audiofile(audio+".mp3")
print(" your video has covertes to audio sucessfully")
print("!! sucess!!")
aud.close()
vid.close()