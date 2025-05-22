import subprocess 
from gpiozero import PWMLED
import time

LED1 = PWMLED(18) # My RED LED
LED2 = PWMLED(26) # My GREEN LED

def is_internet_connected():
    
    try:
        # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    
    except subprocess.CalledProcessError:
        
        return False

def LED_Switch():
    
    if is_internet_connected() == True:
        LED1.off()
        LED2.on()
        time.sleep(0.3)
    
    elif is_internet_connected() == False:
        LED2.off()
        LED1.on()
        time.sleep(0.3)
        
        
def loop():
    while (True):
        is_internet_connected()
        LED_Switch()
        
def destroy():
    LED1.close()
    LED2.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
