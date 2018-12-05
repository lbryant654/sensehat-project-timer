from sense_hat import *
from time import *
sense = SenseHat()

g = [0, 255, 0]
r = [255, 0, 0]
x = [0, 0, 0]
secs = 35

for i in range(64):
    if i < s:
        timer.append(g)
    else:
        timer.append(x)

sense.set_pixels(timer)

for i in range(0, secs):
    sleep(1)
    timer[i] = r
    sense.set_pixels(timer)
