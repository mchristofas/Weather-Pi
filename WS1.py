# Extreme Windsurfing
# WS1.py
# 5/21/17
# surfstandingup@gmail.com



from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # setup BCM GPIO numbering scheme

# Setup input pin
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callbackup function to run in another thread when button pressed
def buttonPressed(channel):
    global counter
    counter += 1
    print "Button Pressed:",counter



# add event listener on pin 18
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonPressed, bouncetime=150)
counter = 0
try:
    while True:
        sleep(1) 


finally:
    GPIO.cleanup()
    print "gpio pins are clean!"
