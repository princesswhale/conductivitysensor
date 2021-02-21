#Frequency to Conductivity Converter

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time 

GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BCM) # Use BCM pin numbering

input_signal = 4
end_time = 0
start_time = 0
capacitor = 0.0000001 #.1 microfarad
resistor1 = 20000 #20 kOhm

GPIO.setup(input_signal,GPIO.IN)

while True:
    while GPIO.input(input_signal) == 0:
        start_time = time.time()

    while GPIO.input(input_signal) == 1:
        end_time = time.time()

    signal_time = end_time - start_time

    if(signal_time != 0):
        freq = (1 / signal_time ) / 2
	conductivity = ((1/(0.7*freq*capacitor))-resistor1)/2
        if (freq > 1):
            print(str(round(freq,1)) + " " + "Hz")
	    print(conductivity) 

        time.sleep(1)  


