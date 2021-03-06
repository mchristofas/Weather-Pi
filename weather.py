#!/usr/bin/python

# import the libraries
import RPi.GPIO as GPIO
import time, math
import datetime
import os
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# define gpio pin to read and set the rotation count to zero
pin = 18
count = 0

# Or create an ADS1015 ADC (12-bit) instance.
adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

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

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('-' * 37)
# Main loop.
try:
    while True:
    # Read all the ADC channel values in a list.
        # Read the specified ADC channel using the previously set gain value.
        wind_dir = adc.read_adc(1, gain=GAIN)
        print "begin"

        count = 0
        time.sleep(interval)
        file = open("/mnt/windows/WeatherInfo.txt","w")
        speed = "  Wind speed: "+ calculate_speed(3.54331, interval)+ "mph"
        speed = str(speed)
        print speed
        file.write(speed)
        file.close()
   
        #print values
        if wind_dir > 1900 and wind_dir < 1970:
            print "N"
            time.sleep(0.5)
        elif wind_dir > 1740 and wind_dir < 1760:
            print wind_dir
            print "N"
            time.sleep(.5)
        elif wind_dir >984 and wind_dir < 987:
            print "NNE"
            time.sleep(.5)
        elif wind_dir > 986 and wind_dir < 1150:
            print "NE"
            time.sleep(.5)
        elif wind_dir > 2045 and wind_dir < 2048:
            print "W"
            time.sleep(0.5)
        elif wind_dir > 694 and wind_dir < 715:
            print "S"
            print wind_dir
            time.sleep(0.5)
        elif wind_dir > 443 and wind_dir < 460:
            print "SE"
            time.sleep(0.5)
        elif wind_dir > 1564 and wind_dir <1569:
            print "SW"
            time.sleep(.5)
        elif wind_dir > 220 and wind_dir < 234:
            print "E"
            time.sleep(0.5)
        elif wind_dir >202 and wind_dir < 210:
            print "NE"
            time.sleep(.5)

    
        else:
            print wind_dir
            # Pause for half a second.
            time.sleep(0.5)
finally:
    GPIO.cleanup()
    print
    print"All the GPIO pins are clean!"
