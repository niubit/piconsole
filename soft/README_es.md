# PiConsole Software

Colección de firmware para PiConsole.

## Lista de firmware

### CoderDojo Twin Cities

* Descripción: Código de los ejemplos que aparecen en la web [MicroPython for Kids](https://www.coderdojotc.org/micropython/), un gran sitio muy recomendable si se quiere avanzar en el aprendizaje del lenguaje Python.
* Directorio: [CoderDojo_Twin_Cities](https://github.com/niubit/piconsole_soft/tree/master/CoderDojo_Twin_Cities)
* Entorno: MicroPython
    * [oled_displays_pot.py](https://github.com/niubit/piconsole_soft/raw/master/CoderDojo_Twin_Cities/oled_displays_pot.py) + [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/CoderDojo_Twin_Cities/ssd1306.py): [OLED Displays > OLED Pot](https://www.coderdojotc.org/micropython/oled/12-oled-pot/)

### MegaGamesCompilationPicoAdafruit

* Descripción: Colección de 16 juegos escritos en C adaptados para Raspberry Pi Pico de [esta versión](https://www.tinyjoypad.com/esp8285) para ESP8266.
* Directorio: [MegaGamesCompilationPicoAdafruit](https://github.com/niubit/piconsole_soft/tree/master/MegaGamesCompilationPicoAdafruit)
* Entorno: Arduino IDE
* Código: https://github.com/tscha70/MegaGamesCompilationPicoAdafruit
* Instalación: [MegaGamesCompilationPicoAdafruit.uf2](https://github.com/niubit/piconsole_soft/raw/master/MegaGamesCompilationPicoAdafruit/MegaGamesCompilationPicoAdafruit.uf2)
* Controles:
    * Cruceta: Direcciones
    * A: Disparo

### MorseCodeCreator

* Descripción: Traductor de código Morse.
* Directorio: [MorseCodeCreator](https://github.com/niubit/piconsole_soft/tree/master/MorseCodeCreator)
* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/MorseCodeCreator.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar el archivo [MorseCodeCreator.py](https://github.com/niubit/piconsole_soft/raw/master/MorseCodeCreator/MorseCodeCreator.py) (renombrar a `main.py` para que se ejecute automáticamente). La salida del programa se produce por el puerto USB, no por pantalla. Hay que conectar un cliente de puerto serie a ese puerto configurado a 115200 baudios.
* Controles:
    * A: Pulso (largo o corto según el tiempo; se enciende el LED rojo en pulso corto o el verde al hacerse largo)

### Phantom Slayer

* Descripción: Versión de juego clásico de Tandy Color Computer Phantom Slayer.
* Directorio: [Phantoms](https://github.com/niubit/piconsole_soft/tree/master/Phantoms)
* Entorno: [VS Code](https://code.visualstudio.com/)
* Código original: [Sitio](https://smittytone.net/pico-phantoms/), [Repo](https://github.com/smittytone/pi-pico)
* Instalación: [phantoms.uf2](https://github.com/niubit/piconsole_soft/raw/master/Phantoms/phantoms.uf2)
* Controles:
    * Arriba: Adelante
    * Abajo: Atrás
    * Derecha: Girar derecha
    * Izquierda: Girar izquierda
    * A: Disparo
    * B: Teletransporte

### Juegos PiConsole

* Descripción: Juegos sencillos MicroPython adaptados al hardware de PiConsole.
* Directorio: [PiConsole_games](https://github.com/niubit/piconsole_soft/tree/master/PiConsole_games)
* Entorno: MicroPython con [IDE web adaptado a PiConsole](https://piconsole.niubit.net/).
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y directorio [lib](https://github.com/niubit/piconsole_soft/tree/master/thumby_mod/lib) de `thumby_mod` (esto mismo se logra automáticamente usando el botón `FORMAT` en el [IDE de Thumby adaptado a PiConsole](https://piconsole.niubit.net/)). Luego cargar los juegos por separado (renombrar a `main.py` para que se ejecute automáticamente).

### Tamaguino

* Descripción: Mascota virtual inspirada en Tamagotchi.
* Directorio: [Tamaguino](https://github.com/niubit/piconsole_soft/tree/master/Tamaguino)
* Entorno: Arduino IDE
* Código original: [Sitio](https://alojzjakob.github.io/Tamaguino/), [Repo](https://github.com/alojzjakob/Tamaguino)
* Instalación: [Tamaguino.ino.uf2](https://github.com/niubit/piconsole_soft/raw/master/Tamaguino/Tamaguino.ino.uf2)
* Controles:
    * Arriba: Menú
    * Abajo: Estado o Aceptar
    * Derecha: Salir

### Colección Cheungbx

* Descripción: Colección de minijuegos Python.
* Directorio: [coleccion_cheungbx](https://github.com/niubit/piconsole_soft/tree/master/coleccion_cheungbx)
* Entorno: MicroPython
* Código original: https://github.com/niubit/gameESP-micropython/
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar la librería [gameESP.py](https://github.com/niubit/piconsole_soft/raw/master/coleccion_cheungbx/gameESP.py). Luego los juegos propiamente dichos (renombrando a `main.py` para que se ejecuten automáticamente).
* Controles:
    * Se puede alternar entre control analógico o digital al pulsar Arriba en el menú de opciones de cada juego.

### Demo Adafruit para SSD1306 SPI

* Descripción: Demo de las capacidades de la librería SSD1306 de Adafruit.
* Directorio: [oled_demo](https://github.com/niubit/piconsole_soft/tree/master/oled_demo)
* Entorno: Arduino IDE
* Código original: https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_spi/ssd1306_128x64_spi.ino
* Instalación: Necesaria librería `Adafruit SSD1306`. [oled_demo.ino.uf2](https://github.com/niubit/piconsole_soft/raw/master/oled_demo/oled_demo.uf2)

### Pico Invaders

* Descripción: Space Invaders de pantalla vertical con control analógico.
* Directorio: [picoinvaders](https://github.com/niubit/piconsole_soft/tree/master/picoinvaders)
* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar los archivos [picoinvaders.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders/picoinvaders.py) (renombrar a `main.py` para que se ejecute automáticamente) y [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders/ssd1306.py).
* Controles:
    * Potenciómetro: Movimiento
    * Disparo automático

### Pico Invaders con botones

* Descripción: Space Invaders de pantalla vertical con control digital.
* Directorio: [picoinvaders_with_buttons](https://github.com/niubit/piconsole_soft/tree/master/picoinvaders_with_buttons)
* Entorno: MicroPython
* Código original: https://github.com/printnplay/Pico-MicroPython/blob/main/PicoInvadersWithButtons.py
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar los archivos [PicoInvadersWithButtons.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders_with_buttons/PicoInvadersWithButtons.py) (renombrar a `main.py` para que se ejecute automáticamente) y [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders_with_buttons/ssd1306.py).
* Controles:
    * Arriba/Abajo: Movimiento (izquierda/derecha)
    * A: Disparo

### Reflejos2

* Descripción: Juego de reflejos para dos jugadores. El código sólo tiene 32 líneas por lo que resulta fácil de seguir y es un ejemplo de lo mucho que se puede hacer con poco código. Al arrancar, se enciende el LED rojo entre 5 y 10 segundos. Los jugadores deben pulsar su botón nada más ver apagarse la luz. Al hacerlo se muestra en pantalla cual de los dos ha sido el más rápido.
* Directorio: [reflejos2](https://github.com/niubit/piconsole_soft/tree/master/reflejos2)
* Entorno: MicroPython
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar el archivo [reflejos2.py](https://github.com/niubit/piconsole_soft/raw/master/reflejos2/reflejos2.py) (renombrar a `main.py` para que se ejecute automáticamente) y [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/reflejos2/ssd1306.py).
* Controles:
    * A: Jugador 1
    * B: Jugador 2

### Test PiConsole

* Descripción: Programa de test de entradas y salidas de PiConsole.
* Directorio: [test_piconsole](https://github.com/niubit/piconsole_soft/tree/master/test_piconsole)
* Entorno: Arduino IDE
* Instalación: Necesaria librería `Adafruit SSD1306`. [test_piconsole.uf2](https://github.com/niubit/piconsole_soft/raw/master/test_piconsole/test_piconsole.uf2)
* Controles:
    * Arriba => Enciende LED IR (visualizarlo a través de la cámara de un teléfono móvil)
    * Izquierda => Enciende LED rojo
    * Derecha => Enciende LED amarillo
    * Abajo => Enciende LED verde
    * Controles A y B => Hace sonar el zumbador
    * Potenciómetro => Controla barra superior en pantalla
    * Fotorresistencia LDR => Controla barra inferior en pantalla

### Juegos Thumby

* Descripción: Juegos hechos para Thumby por la comunidad, compatibles con PiConsole.
* Directorio: [thumby_games](https://github.com/niubit/piconsole_soft/tree/master/thumby_games)
* Entorno: MicroPython con [IDE web adaptado a PiConsole](https://piconsole.niubit.net/).
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y directorio [lib](https://github.com/niubit/piconsole_soft/tree/master/thumby_mod/lib) de `thumby_mod` (esto mismo se logra automáticamente usando el botón `FORMAT` en el [IDE de Thumby adaptado a PiConsole](https://piconsole.niubit.net/)). Luego cargar los juegos por separado (renombrar a `main.py` para que se ejecute automáticamente).

### Adaptación plataforma Thumby

* Descripción: Juegos predeterminados de [Thumby](https://www.indiegogo.com/projects/thumby-the-tiny-playable-keychain#/). Son los mismos juegos que se instalan al usar el botón `FORMAT` en el [IDE de Thumby adaptado a PiConsole](https://piconsole.niubit.net/).
* Directorio: [thumby_mod](https://github.com/niubit/piconsole_soft/tree/master/thumby_mod)
* Entorno: MicroPython con [IDE web adaptado a PiConsole](https://piconsole.niubit.net/).
* Código original: https://github.com/TinyCircuits/tinycircuits.github.io/tree/master/ThumbyGames
* Instalación: Instalar [firmware MicroPython](https://micropython.org/download/rp2-pico/) y cargar todos los archivos siguiendo la estructura de directorios.
* Controles: Cruceta + A + B

## Pines - Componentes

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

## Entorno Arduino IDE

Seguir [estas instrucciones](https://arduino-pico.readthedocs.io/en/latest/install.html#installing-via-arduino-boards-manager) para añadir la Pico como placa soportada en Arduino IDE.

## Librerías

* MicroPython
    * https://github.com/adafruit/micropython-adafruit-ssd1306
    * https://github.com/adafruit/micropython-adafruit-gfx
* CircuitPython
    * https://github.com/adafruit/Adafruit_CircuitPython_SSD1306
    * https://github.com/adafruit/Adafruit_CircuitPython_GFX
