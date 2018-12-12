from sense_hat import *
from time import *
sense = SenseHat()

w = [255, 255, 255]
x = [0, 0, 0]

timer = []

br = (135, 84, 43)
r = (255, 0, 0)
ro = (255, 67, 0)
o = (255, 125, 0)
yo = (255, 175, 0)
y = (255, 255, 0)
yg = (125, 255, 0)
g = (0, 255, 0)
bg = (0, 255, 125)
b = (0, 0, 255)
bv = (125, 0, 255)
v = (255, 0, 255)
p = (255, 0, 125)

blinkblink = [
    r, r, ro, o, yo, y, yg, g,
    r, ro, o, yo, y, yg, g, bg,
    ro, o, yo, y, yg, g, bg, b,
    o, yo, y, yg, g, bg, b, bv,
    yo, y, yg, g, bg, b, bv, v,
    y, yg, g, bg, b, bv, v, p,
    yg, g, bg, b, bv, v, p, r,
    g, bg, b, bv, v, p, r, r
]

scroll_speed = 0.05

def pressed():
    sense.show_message("5 second timer.", text_colour = r, scroll_speed = 0.05)
    sense.show_message("Say the alphabet as fast as you can in this time frame!", text_colour = b, scroll_speed = 0.05)
    secs = 5        
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

def rightt():
    sense.show_message("10 second timer.", text_colour = r, scroll_speed = 0.05)
    sense.show_message("FF", text_colour = b, scroll_speed = 0.05)
    secs = 10       
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


def leftt():
    sense.show_message("20 second timer.", text_colour = r, scroll_speed = 0.05)
    sense.show_message("FF", text_colour = b, scroll_speed = 0.05)
    secs = 20       
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
sense.stick.direction_right = rightt
sense.stick.direction_left = leftt
