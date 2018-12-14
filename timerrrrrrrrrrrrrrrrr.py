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

secs = 0

timerr = True

def pressed():
    global secs
    sense.show_message(str(secs) + " second timer.", text_colour = r, scroll_speed = 0.05)

    if secs <= 5:
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
        global blinkblink
        sense.clear()
        sleep(0.1)
        sense.set_pixels(blinkblink)
        sleep(0.1)

    timerr = False
    sense.clear()

def rightt():
    global secs
    if secs < 9:
        secs += 1
        sense.show_letter(str(secs), text_colour = g)
    elif secs >= 9:
        secs += 1
        sense.show_letter(str((secs - 10)), text_colour = g)
    elif secs >= 19:
        secs += 1
        sense.show_letter(str((secs - 20)), text_colour = g)
    elif secs >= 29:
        secs += 1
        sense.show_letter(str((secs - 30)), text_colour = g)
    elif secs >= 39:
        secs += 1
        sense.show_letter(str((secs - 40)), text_colour = g)
    elif secs >= 49:
        secs += 1
        sense.show_letter(str((secs - 50)), text_colour = g)
    elif secs >= 59 and secs < 64:
        secs += 1
        sense.show_letter(str((secs - 60)), text_colour = g)
    elif secs == 64:
        sense.show_message("You can't go any higher!", text_colour = r)

def leftt():
    global secs
    if secs < 10:
        secs -= 1
        sense.show_letter(str((secs - 10)), text_colour = g)
    elif secs < 20:
        secs -= 1
        sense.show_letter(str((secs - 20)), text_colour = g)
    elif secs < 30:
        secs -= 1
        sense.show_letter(str((secs - 30)), text_colour = g)
    elif secs < 40:
        secs -= 1
        sense.show_letter(str((secs - 40)), text_colour = g)
    elif secs < 50:
        secs -= 1
        sense.show_letter(str((secs - 50)), text_colour = g)
    elif secs < 60:
        secs -= 1
        sense.show_letter(str((secs - 60)), text_colour = g)
while True:
    sense.stick.direction_middle = pressed
    sense.stick.direction_right = rightt
    sense.stick.direction_left = leftt
