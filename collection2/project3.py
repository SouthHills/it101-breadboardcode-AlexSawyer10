# Description : Control RGBLED with Potentiometers
from pathlib import Path
import sys
from gpiozero import RGBLED
import time

from pathlib import Path
path = Path('get_temp.txt')
contents = path.read_text()
string_content = str(content)

RED_LED_PIN = 22      # define 3 pins for RGBLED
GREEN_LED_PIN = 27
BLUE_LED_PIN = 17
RGB_LED = RGBLED(red=RED_LED_PIN, green=GREEN_LED_PIN, blue=BLUE_LED_PIN, pwm=True)

def loop_tempature():
    global string_contents, RGBLED
    
    string_content = string[0,1]
    
    string_content = int
    
    if string_content <= 15:
        BLUE_

if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()



