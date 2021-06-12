import time
from ws2812b import ws2812b

num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0,17)

pixels.fill(0,0,0)
pixels.show()

i = 0
brightness = 0
fadeAmount = 1

while True:
    for i in range(num_leds):
        pixels.set_pixel(i,0,brightness,brightness)
    pixels.show()
    brightness = brightness + fadeAmount
    if brightness <= 0 or brightness >= 200:
        fadeAmount = -fadeAmount
    time.sleep(0.005)