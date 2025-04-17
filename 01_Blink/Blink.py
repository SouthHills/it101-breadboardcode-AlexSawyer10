from gpiozero import LED as LEDClass # Alias
import time

LED = LEDClass(17)  # define led
LED2 = LEDClass(18) 
def loop():
    global LED
    global LED2
    while True:
        LED.on() 
        time.sleep(.8)
        print ("led turned on >>>") # print information on terminal
        LED.off()
        
        print ("led turned off <<<")
        LED2.on()
        time.sleep(.8)
        print ("led turned on >>>") 
        LED2.off()
        print ("led turned off <<<")
        
        
def destroy():
    global LED
    # Release resources
    LED.close()
    LED2.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pin {LED.pin}")
    print(f"Using pin {LED2.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
