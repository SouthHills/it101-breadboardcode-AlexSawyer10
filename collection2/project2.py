import subprocess 
from pathlib import Path
import sys
from gpiozero import PWMLED
import time

# The next two lines are required to be able to properly import ADCDevice
HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

ADC = ADCDevice() # Define an ADCDevice class object
RED = PWMLED(18) 
GREEN = PWMLED(26) 
YELLOW = PWMLED(21) 
BLUE = PWMLED(6)

def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
          
def loop():
    while (True):
        global ADC, LED1, LED2, LED3, LED4

        value = ADC.analogRead(0)  # Gets a value between 0 and 255
    
    
        print(f"Current value: {value}")
    
        if value >= 213.75:
            RED.on() 
            GREEN.on()
            YELLOW.on()
            BLUE.on()
            
        elif value >= 168.75:
            RED.off()
            YELLOW.on()
            GREEN.on()
            BLUE.on()
        
        elif value >= 112.5:
            GREEN.on()
            BLUE.on()
            YELLOW.off()
            RED.off()
            

        elif value >= 63:
            BLUE.on()
            YELLOW.off()
            GREEN.off()
            RED.off()
               
        else:
            GREEN.off()
            YELLOW.off()
            RED.off()
            BLUE.off()
       
        
def destroy():
    global ADC, LED1, LED2, LED3, LED4
    ADC.close()
    RED.close()
    GREEN.close()
    YELLOW.close()
    BLUE.close()
    
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
