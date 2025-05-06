import subprocess
import time
from gpiozero import Button
from signal import pause
BUTTON = Button(18)  # define first buttonPin
BUTTON2 = Button(17) # My second button

firefox_process = None
chrome_process = None

def firefox_Change():
    
    global firefox_process
    if firefox_process is None: 
        # Start the process
        firefox_process = subprocess.Popen(["firefox"])
        time.sleep(25)
    else:
        # Terminate the process
        firefox_process.terminate()
        firefox_process = None
        #commit test
    
def destroy_firefox():
    if firefox_process:
        firefox_process.terminate()
    BUTTON.close()

def chrome_Change():
    global chrome_process
    if chrome_process is None:
        chrome_process = subprocess.Popen(['chromium'])
        time.sleep(25)
    else:
         # Terminate the process
        chrome_process.terminate()
        chrome_process = None
    
def destroy_chrome():
    if chrome_process:
        chrome_process.terminate()
    BUTTON2.close()
    

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = firefox_Change
        BUTTON2.when_pressed = chrome_Change
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy_firefox()
        destroy_chrome()
