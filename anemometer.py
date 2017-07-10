# Anemometer.py
# 5/22/17
# mchristofas@gmail.com


# import the libraries
import RPi.GPIO as GPIO
import time, math
import datetime
import os

# define gpio pin to read and set the rotation count to zero
pin = 18
count = 0


# define the calculate speed call
def calculate_speed(r_in, time_sec):
    global count
    circ_in = (2 * math.pi) * r_in
    rot = count / 1.0
    dist_mile = (circ_in * rot) / 63360 # convert to kilometres
    mile_per_sec = dist_mile / time_sec
    mile_per_hour = mile_per_sec * 3600 # convert to distance per hour
    mph = mile_per_hour
    mph = mph * 1.18 # correction factor for friction, device specific
    mph = "%5.1f" % mph
    return mph
def spin(channel):
    global count
    count += 1
    #print (count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin)

interval = 5
print "begin"
try:
    while True:
        count = 0
        time.sleep(interval)
        file = open("/mnt/windows/WeatherInfo.txt","w")
        speed = "  Wind speed: "+ calculate_speed(3.54331, interval)+ "mph"
        speed = str(speed)
        print speed
        file.write(speed)
        file.close()

finally:
    GPIO.cleanup()
    print
    print"All the GPIO pins are clean!"
