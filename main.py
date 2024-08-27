import time
import pyautogui
import keyboard
from pynput import mouse
from pynput.mouse import Button, Controller

time.sleep(1)

# Define {x, y} coordinantes of the positions to click (modify according to your case)
y = 400 
x1 = 377
x2 = 456
x3 = 538
x4 = 618

positions = [(x1,y), (x2,y), (x3,y), (x4,y)]

# Create an instance of Controller class
mouse = Controller()
def click (x, y):
    # Move pointer to the desired position
    mouse.position = (x,y) # Compensate for the time it takes for the cursor to moves

    # Press and release Left Click of the mouse
    mouse.press(Button.left)
    time.sleep(0.01) # Ensures that the click is registered without slowing down 
    mouse.release(Button.left)

# Setting the Research pattern   
while keyboard.is_pressed("q") == False:
    for i in range (len(positions)):
        x,y = positions[i]
        if pyautogui.pixel(x,y)[0] == 0:
            click(x,y)
            positions.append(positions.pop(i))
          
