from pathlib import Path
import sys
from gpiozero import PWMLED, TonalBuzzer
import time
from signal import pause
import subprocess

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

LED = PWMLED(21)

BUZZER = TonalBuzzer(18)
HIGH_TONE = 600# The max is 880 but that hurts my ears, remember I can change volume to 880 if I want
LOW_TONE = 220 


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
    while (True):
        photo_resistor_trip()
        display_emergency_webpage()
        buzzer_led_turned_on()
        
    

    
def photo_resistor_trip():
    while (True):
        value = ADC.analogRead(0)   # read the ADC value of channel 0  # Mapping to PWM duty cycle        
        voltage = value / 255.0 * 3.3
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} \tLED Value: {LED.value:.2f}')
        time.sleep(0.01)
        
        if value > 60:
            return

def buzzer_led_turned_on():
    print ('Buzzer turned on >>> ')
    while (True):
        for x in range(LOW_TONE, HIGH_TONE): # Remember this rises the tone
            BUZZER.play(x)
            LED.value = (x- LOW_TONE) / (HIGH_TONE - LOW_TONE)
            time.sleep(0.002)
            
        print ("LED Value: {LED.value:.2f}")

            
        for x in range(HIGH_TONE, LOW_TONE, -1): # Remember this lowers the tone
            BUZZER.play(x)
            LED.value = (x - LOW_TONE) / (HIGH_TONE - LOW_TONE)
            time.sleep(0.002)
            
        print ("LED Value: {LED.value:.2f}")



    
def display_emergency_webpage():
    html_process= subprocess.Popen(['chromium','http://127.0.0.1:3000/final_project/EmergencyContactPage.html'])
    



def destroy():
    global ADC, LED, BUZZER
    ADC.close()
    LED.close()
    BUZZER.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        