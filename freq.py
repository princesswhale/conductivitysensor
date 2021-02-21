#Basic LCD Frequency Counter MAX 10KHz

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time 


#import board
#import digitalio
#import adafruit_character_lcd.character_lcd as characterlcd

GPIO.setwarnings(False) # Disable warnings
GPIO.setmode(GPIO.BCM) # Use BCM pin numbering

#lcd_rs = digitalio.DigitalInOut(board.D26)
#lcd_en = digitalio.DigitalInOut(board.D19)
#lcd_d4 = digitalio.DigitalInOut(board.D13)
#lcd_d5 = digitalio.DigitalInOut(board.D6)
#lcd_d6 = digitalio.DigitalInOut(board.D5)
#lcd_d7 = digitalio.DigitalInOut(board.D11)

 
# Modify this if you have a different sized character LCD
#lcd_columns = 20
#lcd_rows = 4


Input_Signal = 4
end_time = 0
start_time = 0
cap = 0.0000001
r1 = 20000

GPIO.setup(Input_Signal,GPIO.IN)

# Initialise the lcd 

#lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,lcd_d7, lcd_columns, lcd_rows)

# wipe LCD screen before we start
#lcd.clear()


while True:
  

    while GPIO.input(Input_Signal) == 0:
        start_time = time.time()

    while GPIO.input(Input_Signal) == 1:
        end_time = time.time()

    signal_time = end_time - start_time
    #
    if(signal_time != 0):
        freq = (1 / signal_time ) / 2
	conductivity = ((1/(0.7*freq*cap))-r1)/2
        if (freq > 1):
            print(str(round(freq,1)) + " " + "Hz")
	    print(conductivity) 

        time.sleep(1)  


