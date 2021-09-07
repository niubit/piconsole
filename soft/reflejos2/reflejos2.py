import utime
import urandom
from machine import Pin, SPI, ADC, PWM
from ssd1306 import SSD1306_SPI

spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 64, spi, Pin(16), Pin(20), Pin(17))

oled.fill(0)
oled.show()

led = Pin(9, Pin.OUT)
pulsador_A = Pin(11, Pin.IN, Pin.PULL_UP)
pulsador_B = Pin(7, Pin.IN, Pin.PULL_UP)

led.on()
utime.sleep(urandom.uniform(5, 10))
led.off()

pulsado_A = False
pulsado_B = False
while not (pulsado_A or pulsado_B):
    pulsado_A = not pulsador_A.value()
    pulsado_B = not pulsador_B.value()

if pulsado_A:
    oled.text("Ha ganado A", 0, 0)
elif pulsado_B:
    oled.text("Ha ganado B", 0, 0)
else:
    oled.text("Ha ganado ?", 0, 0)
oled.show()

