# Pines - Componentes

* Pot
    * ADC1
* LDR
    * ADC2
* LED
    * GP8 -> Amarillo
    * GP9 -> Rojo
    * GP21 -> Verde
    * GP22 -> IR
* Buzzer
    * GP10
* Controles
    * GP11 -> Disparo
    * GP12 -> Derecha
    * GP13 -> Izquierda
    * GP14 -> Abajo
    * GP15 -> Arriba
* OLED
    * GP16 -> DC
    * GP17 -> CS
    * GP18 -> SCL
    * GP19 -> SDA
    * GP20 -> RES

# Entorno Arduino IDE

Seguir [estas instrucciones](https://arduino-pico.readthedocs.io/en/latest/install.html#installing-via-arduino-boards-manager) para añadir la Pico como placa soportada en Arduino IDE.

# Librerías

* MicroPython
    * https://github.com/adafruit/micropython-adafruit-ssd1306
    * https://github.com/adafruit/micropython-adafruit-gfx
* CircuitPython
    * https://github.com/adafruit/Adafruit_CircuitPython_SSD1306
    * https://github.com/adafruit/Adafruit_CircuitPython_GFX

# Juegos para intentar portar

https://github.com/AJRussell/Tiny-Tetris
https://github.com/cheungbx/game8266-micropython
https://github.com/cheungbx/gameESP-micropython
http://www.crait.net/

# Soft

## Test PiConsole

* Entorno: Arduino IDE
* Librerías: Necesaria librería `Adafruit SSD1306`
* Instalación: test_piconsole.uf2

## Demo Adafruit para SSD1306 SPI

* Entorno: Arduino IDE
* Código original: https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_spi/ssd1306_128x64_spi.ino
* Librerías: Necesaria librería `Adafruit SSD1306`
* Instalación: oled_demo.uf2

## MegaGamesCompilationPicoAdafruit

* Entorno: Arduino IDE
* Código: https://github.com/tscha70/MegaGamesCompilationPicoAdafruit
* Instalación: MegaGamesCompilationPicoAdafruit.uf2

## Pico Invaders

* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar los archivos `picoinvaders.py` (renombrar a `main.py` para que se ejecute automáticamente) y `ssd1306.py`.

## coleccion_cheungbx

* Entorno: MicroPython
* Código original: https://github.com/niubit/gameESP-micropython/
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar la librería `gameESP.py`. Luego los juegos propiamente dichos (renombrando a `main.py` para que se ejecuten automáticamente).
