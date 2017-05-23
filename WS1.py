from time import sleep
import RPi.GPIO as GPIO
from read_RPM import reader
import pigpio

GPIO.setmode(GPIO.BCM) # setup BCM GPIO numbering scheme

# connect to pigpio
pi = pigpio.pi()

# Setup input pin
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)



# Setup RPM reader
RPM_GPIO = 18
SAMPLE_TIME = 2.0
tach = reader(pi, RPM_GPIO)



# Callbackup function to run in another thread when button pressed
def buttonPressed(channel):
    global counter
    counter += .5
    print "Switch Released:",counter
    rpm  = tach.RPM()/2
    mph = rpm/30*1.492
    rpm = "%10.2f" % rpm
    print "RPM:",rpm
    mph = "%10.2f" % mph
    print "Wind Speed: ",mph," mph"



# add event listener on pin 18
# event will interrupt the program and call the buttonPressed function
GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonPressed, bouncetime=25)
counter = 0
try:
    while True:
        sleep(1) 


    
except KeyboardInterrupt:
    GPIO.cleanup()
    print
    print "gpio pins are cleaner!"


