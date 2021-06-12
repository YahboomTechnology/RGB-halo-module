import time
import ws2812b
import random

numpix = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
strip = ws2812b.ws2812b(numpix, 0,17)
    
strip.fill(0,0,0)

while True:
    for i in range(numpix):
        #pixel_num, red, green, blue
        strip.set_pixel(i, 0, 255, 0)
        time.sleep(0.005)
        strip.show()
