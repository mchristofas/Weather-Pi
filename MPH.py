# Anemometer.py
# 5/22/17
# mchristofas@gmail.com


# import the libraries
import RPi.GPIO as GPIO
import time, math
import datetime

# define gpio pin to read and set the rotation count to zero
pin = 18
count = 0


# define the calculate speed call
def calculate_speed(r_cm, time_sec):
    global count
    circ_cm = (2 * math.pi) * r_cm
    rot = count / 2.0
    dist_km = (circ_cm * rot) / 100000.0 # convert to kilometres
    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * 3600 # convert to distance per hour
    mph = km_per_hour * 0.62137119223733 # convert to mph
    mph = mph * 1.18 # correction factor for friction, device specific
    mph = "%5.2f" % mph
    #print "Mph:",mph
    #print "Km/h:",km_per_hour
    return mph
def spin(channel):
    global count
    count += 1
    #print (count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin)

interval = 5


try:
    while True:
        count = 0
        time.sleep(interval)
        print "Wind speed:", calculate_speed(9.0, interval), "mph"
finally:
    GPIO.cleanup()
    print
    print"All the GPIO pins are clean!"
