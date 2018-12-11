from sense_hat import *
from time import *
sense = SenseHat()

b = [0, 0, 255]
g = [0, 255, 0]
r = [255, 0, 0]
w = [255, 255, 255]
x = [0, 0, 0]
secs = 5

timer = []

blinkblink = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
    ]

def pressed():
    sense.show_message("5 second timer.", text_colour = r, scroll_speed = 0.05)
    sense.show_message("Say the alphabet as fast as you can in this time frame!", text_colour = b, scroll_speed = 0.05)
            
    for i in range(64):
        if i < secs:
            timer.append(g)
        else:
            timer.append(x)

    sense.set_pixels(timer)

    for i in range(0, secs):
        sleep(1)
        timer[i] = r
        sense.set_pixels(timer)
    
    for i in range(0,10):
        sense.clear()
        sleep(0.1)
        sense.set_pixels(blinkblink)
        sleep(0.1)

    sense.clear()

sense.stick.direction_middle = pressed

while True:
    pass
