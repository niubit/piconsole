import machine
import utime
from machine import Pin, SPI
from ssd1306 import SSD1306_SPI

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

pot_pin = machine.ADC(1)
spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))

# Screen size
width=128
height=64
half_height = int(height / 2)
# oled = SSD1306_I2C(width, height, i2c)
oled = SSD1306_SPI(WIDTH, HEIGHT, spi, Pin(16), Pin(20), Pin(17))                  # Init oled display

oled.fill(0) # clear to black

# note that OLEDs have problems with screen burn it - don't leave this on too long!
def border(width, height):
    oled.hline(0, 0, width - 1, 1) # top edge
    oled.hline(0, height - 2, width - 1, 1) # bottom edge
    oled.vline(0, 0, height - 1, 1) # left edge
    oled.vline(width - 1, 0, height - 1, 1) # right edge

# Takes an input number vale and a range between high-and-low and returns it scaled to the new range
# This is similar to the Arduino map() function
def valmap(value, istart, istop, ostart, ostop):
  return int(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

# draw a horizontal bar
def draw_hbar(inval, height, state):
    oled.fill(0) # clear screen
    border(width, height) # draw a border
    oled.fill_rect(0, 1, inval, height, 1) # fill with 1
    utime.sleep(.1) # wait a bit

# continuous update
while True:
    pot_val = int(pot_pin.read_u16())
    # the max value of the input is a 2^16 or 65536
    pot_scaled = valmap(pot_val, 0, 65536, 0, 127)
    print(pot_val, pot_scaled)
    draw_hbar(pot_scaled, half_height, 1)

    oled.text('raw:', 0, half_height + 5, 1)
    oled.text(str(pot_val), 30, half_height + 5, 1)

    oled.text('scaled:', 0, half_height + 15, 1)
    oled.text(str(pot_scaled), 60, half_height + 15, 1)
    oled.show()  
