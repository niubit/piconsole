# PiConsole Software

Firmware collection for PiConsole.

## Firmware list

### CoderDojo Twin Cities

* Description: Code from the examples that appear on the [MicroPython for Kids](https://www.coderdojotc.org/micropython/) website, a great site that is highly recommended if you want to advance in learning the Python language.
* Folder: [CoderDojo_Twin_Cities](https://github.com/niubit/piconsole_soft/tree/master/CoderDojo_Twin_Cities)
* Environment: MicroPython
    * [oled_displays_pot.py](https://github.com/niubit/piconsole_soft/raw/master/CoderDojo_Twin_Cities/oled_displays_pot.py) + [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/CoderDojo_Twin_Cities/ssd1306.py): [OLED Displays > OLED Pot](https://www.coderdojotc.org/micropython/oled/12-oled-pot/)

### MegaGamesCompilationPicoAdafruit

* Description: Collection of 16 games written in C adapted for Raspberry Pi Pico from [this version](https://www.tinyjoypad.com/esp8285) for ESP8266.
* Folder: [MegaGamesCompilationPicoAdafruit](https://github.com/niubit/piconsole_soft/tree/master/MegaGamesCompilationPicoAdafruit)
* Environment: Arduino IDE
* Code: https://github.com/tscha70/MegaGamesCompilationPicoAdafruit
* Installation: [MegaGamesCompilationPicoAdafruit.uf2](https://github.com/niubit/piconsole_soft/raw/master/MegaGamesCompilationPicoAdafruit/MegaGamesCompilationPicoAdafruit.uf2)
* Controls:
    * D-pad: Directions
    * A: Fire

### MorseCodeCreator

* Description: Morse code translator.
* Folder: [MorseCodeCreator](https://github.com/niubit/piconsole_soft/tree/master/MorseCodeCreator)
* Environment: MicroPython
* Original code: https://github.com/printnplay/Pico-MicroPython/blob/main/MorseCodeCreator.py
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and load the file [MorseCodeCreator.py](https://github.com/niubit/piconsole_soft/raw/master/MorseCodeCreator/MorseCodeCreator.py) (rename as `main.py` for autorun). The output of the program is produced by the USB port, not by the screen. A serial port client must be connected to that port set to 115200 baud.
* Controls:
    * A: Pulse (long or short depending on the time; the red LED lights up when the pulse is short or the green LED lights up when the pulse is long.)

### Phantom Slayer

* Description: Classic game version of Tandy Color Computer Phantom Slayer.
* Folder: [Phantoms](https://github.com/niubit/piconsole_soft/tree/master/Phantoms)
* Environment: [VS Code](https://code.visualstudio.com/)
* Original code: [Site](https://smittytone.net/pico-phantoms/), [Repo](https://github.com/smittytone/pi-pico)
* Installation: [phantoms.uf2](https://github.com/niubit/piconsole_soft/raw/master/Phantoms/phantoms.uf2)
* Controls:
    * Up: Forward
    * Down: Backward
    * Right: Turn right
    * Left: Turn left
    * A: Fire
    * B: Teleport

### PiConsole games

* Description: Simple MicroPython games adapted to the PiConsole hardware.
* Folder: [PiConsole_games](https://github.com/niubit/piconsole_soft/tree/master/PiConsole_games)
* Environment: MicroPython with [web IDE adapted to PiConsole](https://piconsole.niubit.net/).
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and [lib](https://github.com/niubit/piconsole_soft/tree/master/thumby_mod/lib) directory from `thumby_mod` (this is automatically achieved by using the `FORMAT` button in the [Thumby IDE adapted to PiConsole](https://piconsole.niubit.net/)). Then load the games separately (rename as `main.py` for autorun).

### Tamaguino

* Description: Virtual pet inspired by Tamagotchi.
* Folder: [Tamaguino](https://github.com/niubit/piconsole_soft/tree/master/Tamaguino)
* Environment: Arduino IDE
* Original code: [Site](https://alojzjakob.github.io/Tamaguino/), [Repo](https://github.com/alojzjakob/Tamaguino)
* Installation: [Tamaguino.ino.uf2](https://github.com/niubit/piconsole_soft/raw/master/Tamaguino/Tamaguino.ino.uf2)
* Controls:
    * Up: Menu
    * Down: Status or Accept
    * Right: Back

### Picotamachibi

* Description: Virtual pet inspired by Tamagotchi.
* Folder: [picotamachibi](https://github.com/niubit/piconsole_soft/tree/master/picotamachibi)
* Environment: MicroPython with [web IDE adapted to PiConsole](https://piconsole.niubit.net/).
* Original code: https://github.com/kevinmcaleer/picotamachibi
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/). Then load all the files from folder (rename `picotamachibi.py` as `main.py` for autorun).
* Controls:
    * Right: Select
    * A: Accept
    * B: Back

### Colección Cheungbx

* Description: Collection of Python mini-games.
* Folder: [coleccion_cheungbx](https://github.com/niubit/piconsole_soft/tree/master/coleccion_cheungbx)
* Environment: MicroPython
* Original code: https://github.com/niubit/gameESP-micropython/
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and load the [gameESP.py](https://github.com/niubit/piconsole_soft/raw/master/coleccion_cheungbx/gameESP.py) library. Then the games themselves (rename as `main.py` for autorun).
* Controls:
    * You can toggle between analogue and digital control by pressing Up in the options menu of each game.

### Demo Adafruit para SSD1306 SPI

* Description: Demo of the capabilities of the Adafruit SSD1306 library.
* Folder: [oled_demo](https://github.com/niubit/piconsole_soft/tree/master/oled_demo)
* Environment: Arduino IDE
* Original code: https://github.com/adafruit/Adafruit_SSD1306/blob/master/examples/ssd1306_128x64_spi/ssd1306_128x64_spi.ino
* Installation: Required `Adafruit SSD1306` library. [oled_demo.ino.uf2](https://github.com/niubit/piconsole_soft/raw/master/oled_demo/oled_demo.uf2)

### Pico Invaders

* Description: Vertical screen Space Invaders with analogue control.
* Folder: [picoinvaders](https://github.com/niubit/piconsole_soft/tree/master/picoinvaders)
* Environment: MicroPython
* Original code: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and load the files [picoinvaders.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders/picoinvaders.py) (rename as `main.py` for autorun) and [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders/ssd1306.py).
* Controls:
    * Potentiometer: Movement
    * Auto fire

### Pico Invaders with buttons

* Description: Vertical screen Space Invaders with digital control.
* Folder: [picoinvaders_with_buttons](https://github.com/niubit/piconsole_soft/tree/master/picoinvaders_with_buttons)
* Environment: MicroPython
* Original code: https://github.com/printnplay/Pico-MicroPython/blob/main/PicoInvadersWithButtons.py
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and load the files [PicoInvadersWithButtons.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders_with_buttons/PicoInvadersWithButtons.py) (rename as `main.py` for autorun) and [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/picoinvaders_with_buttons/ssd1306.py).
* Controls:
    * Up/Down: Movement (left/right)
    * A: Fire

### Reflejos2

* Description: A reaction game for two players. The code is only 32 lines long so it is easy to follow and is an example of how much can be done with few lines of code. On start-up, the red LED lights up for 5 to 10 seconds. Players must press their button as soon as they see the light go out. When they do so, the screen shows which of the two players was the fastest.
* Folder: [reflejos2](https://github.com/niubit/piconsole_soft/tree/master/reflejos2)
* Environment: MicroPython
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and load the files [reflejos2.py](https://github.com/niubit/piconsole_soft/raw/master/reflejos2/reflejos2.py) (rename as `main.py` for autorun) and [ssd1306.py](https://github.com/niubit/piconsole_soft/raw/master/reflejos2/ssd1306.py).
* Controls:
    * A: Player 1
    * B: Player 2

### Test PiConsole

* Description: PiConsole I/O test program.
* Folder: [test_piconsole](https://github.com/niubit/piconsole_soft/tree/master/test_piconsole)
* Environment: Arduino IDE
* Installation: Librería `Adafruit SSD1306` needed. [test_piconsole.uf2](https://github.com/niubit/piconsole_soft/raw/master/test_piconsole/test_piconsole.uf2)
* Controls:
    * Up: Lights up IR LED (view it through a mobile phone camera)
    * Left: Lights up red LED
    * Right: Lights up yellow LED
    * Down: Lights up green LED
    * A y B: Beeps
    * Potentiometer: Controls top bar on screen
    * Photoresistor LDR: Controls bottom bar on screen

### Games Thumby

* Description: Games made for Thumby by the community, compatible with PiConsole.
* Folder: [thumby_games](https://github.com/niubit/piconsole_soft/tree/master/thumby_games)
* Environment: MicroPython with [web IDE adapted to PiConsole](https://piconsole.niubit.net/).
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and [lib](https://github.com/niubit/piconsole_soft/tree/master/thumby_mod/lib) directory from `thumby_mod` (this is automatically achieved by using the `FORMAT` button in the [Thumby IDE adapted to PiConsole](https://piconsole.niubit.net/)). Then load the games separately (rename to `main.py` to make it run automatically).

### Adaptation of the Thumby platform

* Description: [Thumby](https://www.indiegogo.com/projects/thumby-the-tiny-playable-keychain#/) default games. These are the same games that are installed by using the `FORMAT` button in the [Thumby IDE adapted to PiConsole](https://piconsole.niubit.net/).
* Folder: [thumby_mod](https://github.com/niubit/piconsole_soft/tree/master/thumby_mod)
* Environment: MicroPython with [web IDE adapted to PiConsole](https://piconsole.niubit.net/).
* Original code: https://github.com/TinyCircuits/tinycircuits.github.io/tree/master/ThumbyGames
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and upload all the files following the directory structure.
* Controls: D-pad + A + B

### CHIP-8 emulator

* Description: [CHIP-8](https://es.wikipedia.org/wiki/CHIP-8) virtual system emulator.
* Folder: [chip-8_emulator](https://github.com/niubit/piconsole_soft/tree/master/chip-8_emulator)
* Environment: MicroPython with [web IDE adapted to PiConsole](https://piconsole.niubit.net/).
* Original code: https://github.com/Wireframe-Magazine/Wireframe-54/tree/main/emulator-guide/pychip8
* Installation: Install [firmware MicroPython](https://micropython.org/download/rp2-pico/) and upload all the files following the directory structure.
* Controls: D-pad + A + B mapped in file `cpu.py`

## Pins - Components

* Pot
    * ADC1
* LDR
    * ADC2
* LED
    * GP8 -> Yellow
    * GP9 -> Red
    * GP21 -> Green
    * GP22 -> IR
* Buzzer
    * GP10
* Controls
    * GP11 -> Fire A
    * GP7  -> Fire B
    * GP12 -> Right
    * GP13 -> Left
    * GP14 -> Down
    * GP15 -> Up
* OLED
    * GP16 -> DC
    * GP17 -> CS
    * GP18 -> SCL  //SCK
    * GP19 -> SDA  //MOSI
    * GP20 -> RES

## Arduino IDE environment

Follow [this instructions](https://arduino-pico.readthedocs.io/en/latest/install.html#installing-via-arduino-boards-manager) to add the Pico as a supported board in Arduino IDE.

## Libraries

* MicroPython
    * https://github.com/adafruit/micropython-adafruit-ssd1306
    * https://github.com/adafruit/micropython-adafruit-gfx
* CircuitPython
    * https://github.com/adafruit/Adafruit_CircuitPython_SSD1306
    * https://github.com/adafruit/Adafruit_CircuitPython_GFX
