from gpiozero import LED as LEDClass # Alias
import time

LED = LEDClass(17)  # define red LED
LED2 = LEDClass(18) # define yellow LED
LED3 = LEDClass(27) # define Green LED

def red():
    global LED
    LED.on()
    time.sleep(5)
    LED.off()

def green():
    global LED3
    print("Green light on")
    LED3.on()
    time.sleep(7)
    LED3.off()

    
def yellow():
    global LED2
    print("Yellow Light ON")
    LED2.on()
    time.sleep(2)
    LED2.off()
    
def destroy():
    LED.close()
    LED2.close()
    LED3.close()
    
def trafficLoop():
    while (True):
        red()
        green()
        yellow()
    
if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using Red LED {LED.pin}")
    print(f"Using pin {LED2.pin}")
    try:
        trafficLoop()
        
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
