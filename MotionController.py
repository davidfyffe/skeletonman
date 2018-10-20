import RPi.GPIO as GPIO # Remember to run as superuser (sudo)
import time
import skeletonManRest as skeletonManRest
import thread

class MotionController(object):

    IS_RUNNING = False

    'Common controller class. takes pin number'
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        GPIO.setmode(GPIO.BCM)   # This example uses the BCM pin numbering
        GPIO.setup(self.gpio_pin, GPIO.IN)
        GPIO.add_event_detect(self.gpio_pin, GPIO.RISING, callback=self.MOTION)

    def MOTION(self, gpio_pin):
        if self.IS_RUNNING == False:
            self.IS_RUNNING = True
            print "motion detect"
            thread.start_new_thread(skeletonManRest.callServo, (0,))
            thread.start_new_thread(skeletonManRest.callServo, (2,))
            thread.start_new_thread(skeletonManRest.callServo, (3,))
            #call sounds sync so it waits on the finish
            skeletonManRest.callScarySounds()
            self.IS_RUNNING = False
            print "motion detect end"
        

#motionController.MOTION(self, 1)
