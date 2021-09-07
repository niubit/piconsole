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
    * GP11 -> Disparo A
    * GP7  -> Disparo B
    * GP12 -> Derecha
    * GP13 -> Izquierda
    * GP14 -> Abajo
    * GP15 -> Arriba
* OLED
    * GP16 -> DC
    * GP17 -> CS
    * GP18 -> SCL  //SCK
    * GP19 -> SDA  //MOSI
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

# Soft

## Test PiConsole

* Entorno: Arduino IDE
* Librerías: Necesaria librería `Adafruit SSD1306`
* Instalación: test_piconsole.uf2

## Demo Adafruit para SSD1306 SPI (oled_demo)

* Entorno: Arduino IDE
* Código original: https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_spi/ssd1306_128x64_spi.ino
* Librerías: Necesaria librería `Adafruit SSD1306`
* Instalación: oled_demo.ino.uf2

## MegaGamesCompilationPicoAdafruit

* Entorno: Arduino IDE
* Código: https://github.com/tscha70/MegaGamesCompilationPicoAdafruit
* Instalación: MegaGamesCompilationPicoAdafruit.uf2

## Pico Invaders (picoinvaders)

* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar los archivos `picoinvaders.py` (renombrar a `main.py` para que se ejecute automáticamente) y `ssd1306.py`.

## Pico Invaders con botones (picoinvaders_with_buttons)

* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/PicoInvadersWithButtons.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar los archivos `PicoInvadersWithButtons.py` (renombrar a `main.py` para que se ejecute automáticamente) y `ssd1306.py`.

## Colección Cheungbx (coleccion_cheungbx)

* Entorno: MicroPython
* Código original: https://github.com/niubit/gameESP-micropython/
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar la librería `gameESP.py`. Luego los juegos propiamente dichos (renombrando a `main.py` para que se ejecuten automáticamente).

## Tamaguino

* Entorno: Arduino IDE
* Código original: [Sitio](https://alojzjakob.github.io/Tamaguino/), [Repo](https://github.com/alojzjakob/Tamaguino)
* Instalación: Tamaguino.ino.uf2
* Controles:
    * Arriba: Menú
    * Abajo: Select
    * Derecha: Back

## Phantom Slayer (Phantoms)

* Entorno: VS Code
* Código original: [Sitio](https://smittytone.net/pico-phantoms/), [Repo](https://github.com/niubit/pi-pico/tree/main/phantoms)
* Instalación: phantoms.uf2
* Controles:
    * Arriba: Adelante
    * Abajo: Atrás
    * Derecha: Girar derecha
    * Izquierda: Girar izquierda
    * A: Disparo
    * B: Teletransporte

## MorseCodeCreator

* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/MorseCodeCreator.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar el archivo `MorseCodeCreator.py` (renombrar a `main.py` para que se ejecute automáticamente). La salida del programa se produce por el puerto USB/Serie.
* Controles:
    * A: Pulso (largo o corto según el tiempo; se enciende el LED rojo en pulso corto o el verde al hacerse largo)

## CoderDojo Twin Cities (CoderDojo_Twin_Cities)

* Entorno: MicroPython
* Código original: https://www.coderdojotc.org/micropython/

## Reflejos2

* Entorno: MicroPython
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar el archivo `reflejos2.py` (renombrar a `main.py` para que se ejecute automáticamente).
* Instrucciones: Al arrancar, se enciende el LED rojo entre 5 y 10 segundos. Los jugadores deben pulsar su botón nada más ver apagarse la luz.
* Controles:
    * A: Jugador 1
    * B: Jugador 2
