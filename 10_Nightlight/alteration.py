# Description : Control LED with Photoresistor
from pathlib import Path
import sys
from gpiozero import LEDBarGraph
from time import sleep
import time

LED_PINS : list[int] = [17, 18, 27, 22, 23, 24, 25, 12, 21, 20]
LEDS = LEDBarGraph(*LED_PINS, active_high=False)

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

ADC = ADCDevice() # Define an ADCDevice class object

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
    global ADC, LED
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0
        bar_graph_light = int((value / 255.0) * 10)
        
        if value == 0:
            LEDS.value = 0
            
        else:
            LEDS.value = bar_graph_light / 10
            
        voltage = value / 255.0 * 3.3 
        
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} \tLED Value: {LEDS.value:.2f}')

        time.sleep(0.01)

def destroy():
    global ADC, LEDS
    ADC.close()
    LEDS.off()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        
