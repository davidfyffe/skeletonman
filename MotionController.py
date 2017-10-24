import RPi.GPIO as GPIO # Remember to run as superuser (sudo)
import time

class MotionController(object):

    
    'Common controller class. takes pin number'
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)   # This example uses the BCM pin numbering
        GPIO.setup(self.gpio_pin, GPIO.IN)
        GPIO.add_event_detect(self.gpio_pin, GPIO.RISING, callback=self.MOTION)

    def MOTION(gpio_pin):
        print "motion detect"
