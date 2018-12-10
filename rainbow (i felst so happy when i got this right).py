from sense_hat import SenseHat

sense = SenseHat()

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

owo_pixels = [
    r, r, ro, o, yo, y, yg, g,
    r, ro, o, yo, y, yg, g, bg,
    ro, o, yo, y, yg, g, bg, b,
    o, yo, y, yg, g, bg, b, bv,
    yo, y, yg, g, bg, b, bv, v,
    y, yg, g, bg, b, bv, v, p,
    yg, g, bg, b, bv, v, p, r,
    g, bg, b, bv, v, p, r, r
]

sense.set_pixels(owo_pixels)
