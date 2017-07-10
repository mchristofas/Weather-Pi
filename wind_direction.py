#!/usr/bin/python
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

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

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('-' * 37)
# Main loop.
while True:
    # Read all the ADC channel values in a list.
        # Read the specified ADC channel using the previously set gain value.
    wind_dir = adc.read_adc(1, gain=GAIN)
       
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
