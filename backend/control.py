import picar_4wd as fc
import time

# left: 30, 3
# right: 30, 3

def turn_left():
    fc.turn_left(30)
    time.sleep(1.8)

def turn_right():
    fc.turn_right(30)
    time.sleep(1.8)

def move_forward():
    fc.forward(1)
    time.sleep(0.02)
    
def move_backward():
    fc.backward(1)
    time.sleep(0.02)
