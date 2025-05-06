from gpiozero import RGBLED, Button
import time
import random

LED = RGBLED(red=17, green=18, blue=27, active_high=True)



BUTTON = Button(23)#define buttonPin



color_names = ["red","yellow","green","blue"]

def colorSet(current_color):
    if current_color == "red":
        LED.color = (1,0,0)
    elif current_color == "green":
        LED.color = (0,1,0)
    elif current_color == "yellow":
        LED.color =(1,1,0)
    elif current_color == "blue":
        LED.color = (0,0,1)
    elif current_color == "none":
        LED.color = (0,0,0)
        

def colorFlash(current_color):
    for i in range (5):
        colorSet(current_color)
        time.sleep(.2)
        colorSet("none")
        time.sleep(.2)
        

def cycleUntilGreen():
    while (True):
         current_color = random.choice(color_names)
         colorSet(current_color)
         time.sleep(1)
         if current_color == "green":
             return current_color
         
            
def runningGame():

    previous_color = cycleUntilGreen()
    
    if previous_color == "green":
        

        if BUTTON.is_pressed:
            if previous_color == "green":
                colorFlash("green")
            else:
                colorFlash("red")
            break
        
    colorSet("none")
    
    
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    
    try:
        runningGame()
        
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        colorSet("none")
    

        
        


