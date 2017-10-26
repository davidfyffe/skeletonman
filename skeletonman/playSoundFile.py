import os
import espeak as talker

def play_sound():
    #os.system('aplay /home/pi/skeletonMan/skeletonman/sound.wav')
    os.system('say hello')

def speak_shit(text):

    #talker.say(text)

    command = "say " + text
    os.system(command)