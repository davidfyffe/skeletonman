import requests


def callServo(servoNum):
    r = requests.get('http://192.168.0.16:8000/skeletonman/servo/'+str(servoNum)+'/')
    print r.text

def callScarySounds():
    r = requests.get('http://192.168.0.16:8000/skeletonman/scarysounds/')
    print r.text
