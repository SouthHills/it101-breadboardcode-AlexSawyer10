from gpiozero import LED as LEDClass, Button
from signal import pause

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
switch = False
def changeLedState():
    global LED
    global switch
    switch = not switch
    if switch == True:
        LED.blink()
        print("led turned on >>>")
    elif switch == False:
        LED.off()
        print ("led turned off >>>")
    

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = changeLedState
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

