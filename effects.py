import time
from sense_hat import SenseHat

def Fill(c):
    pixels=[]
    sense = SenseHat()
    for x in range(0,8):
        for y in range(0,8):
            pixels.append(c)
    sense.set_pixels(pixels)

pixels = [
        [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
        [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
        [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
        [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
        [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
        [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
        [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
        [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]
    

def rainbow():
    sense = SenseHat()

    def next_colour(pix):
        r = pix[0]
        g = pix[1]
        b = pix[2]

        if (r == 255 and g < 255 and b == 0):
            g += 1

        if (g == 255 and r > 0 and b == 0):
            r -= 1

        if (g == 255 and b < 255 and r == 0):
            b += 1

        if (b == 255 and g > 0 and r == 0):
            g -= 1

        if (b == 255 and r < 255 and g == 0):
            r += 1

        if (r == 255 and b > 0 and g == 0):
            b -= 1

        pix[0] = r
        pix[1] = g
        pix[2] = b

    for i in range(0,8*256):
        for pix in pixels:
                next_colour(pix)
        sense.set_pixels(pixels)
        #time.sleep(1.0/(8*256))

def alarm_flash(c,duration=30):
    for d in range(0,duration):
        for t in range(0,10):
            Fill([0,0,0])
            time.sleep(0.2)
            Fill(c)
            time.sleep(0.2)

def pulse_in(c):
    radiusSq = 0.25;
    sense = SenseHat()
    while radiusSq <= 26:
        pixels = []
        #radiusSq = radius * radius
        y = -3.5
        while y <= 3.5:
            x = -3.5
            while x <= 3.5:
                rsq = x * x + y * y
                if rsq <= radiusSq:
                    pixels.append(c)
                else:
                    pixels.append([0, 0, 0])
                x += 1.0
            y += 1.0
        sense.set_pixels(pixels)
        radiusSq += 1.0
        #time.sleep(0.02)

def pulse_raw(c,rSqFrom,rSqTo,rSqDelta):
    radiusSq = rSqFrom;
    sense = SenseHat()
    while (rSqTo-radiusSq)*rSqDelta>-abs(rSqDelta):
        pixels = []
        y = -3.5
        while y <= 3.5:
            x = -3.5
            while x <= 3.5:
                rsq = x * x + y * y
                if rsq <= radiusSq:
                    pixels.append(c)
                else:
                    pixels.append([0, 0, 0])
                x += 1.0
            y += 1.0
        sense.set_pixels(pixels)
        radiusSq += rSqDelta
        #time.sleep(0.02)

def pulse(c):
    pulse_raw(c,0,26,0.8)
    pulse_raw(c,26,0,-0.8)