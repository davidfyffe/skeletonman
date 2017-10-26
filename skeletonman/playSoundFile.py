import os

def play_sound():
    #os.system('aplay /home/pi/skeletonMan/skeletonman/sound.wav')
    os.system('say hello')

def speak_shit(text):
    command = "say " + text
    os.system(command)