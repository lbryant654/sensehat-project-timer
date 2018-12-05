from sense_hat import *
from time import *
sense = SenseHat()

g = [0, 255, 0]

for i in range(5, -1, -1):
    sense.show_letter(str(i), g)
    sleep(1)
